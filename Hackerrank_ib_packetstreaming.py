#from collections import deque

def simulate_packet_streaming(packets, window_size):
    buffer = set()
    played = set()
    play_order = []
    duplicates = []
    next_to_play = 1
    i = 0
    position = 0
    first_duplicate_pos = -1

    while i < len(packets):
        batch = packets[i : i + window_size]
        i += window_size

        for packet in batch:
            if packet in played or packet in buffer:
                duplicates.append(packet)                  # track duplicate packet
                if first_duplicate_pos == -1:
                    first_duplicate_pos = position         # capture first duplicate position
            else:
                buffer.add(packet)
                play_order.append(packet)                  # valid packet into stream list

                while next_to_play in buffer:
                    buffer.remove(next_to_play)
                    played.add(next_to_play)
                    next_to_play += 1
                    position += 1

    if duplicates:
        return play_order, duplicates, first_duplicate_pos
    else:
        return play_order, -1


# Test 1 - has duplicates
packets = [1, 2, 3, 4, 4, 5]
print(simulate_packet_streaming(packets, 3))
# Output: ([1, 2, 3, 4, 5], [4], 4)

# Test 2 - no duplicates
packets2 = [1, 2, 3, 4, 5]
print(simulate_packet_streaming(packets2, 3))
# Output: ([1, 2, 3, 4, 5], -1)