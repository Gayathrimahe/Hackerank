def find_missing_numbers(arr):
    # Remove duplicates and sort the array
    arr = sorted(set(arr))

    # Find missing numbers
    missing = []

    for i in range(arr[0], arr[-1] + 1):
        if i not in arr:
            missing.append(i)

    # Display results
    if missing:
        print("Missing numbers:")
        print(",".join(map(str, missing)))
    else:
        print("No missing numbers found")


# Example usage
numbers = [1, 2, 4, 6, 7, 10]

find_missing_numbers(numbers)