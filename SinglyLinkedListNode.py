"""Given pointers to the heads of two sorted linked lists, merge them into a single, sorted linked list. Either head pointer may be null meaning that the corresponding list is empty.

Example
 refers to 
 refers to 

The new list is 

Function Description

Complete the mergeLists function in the editor below.

mergeLists has the following parameters:

SinglyLinkedListNode pointer headA: a reference to the head of a list
SinglyLinkedListNode pointer headB: a reference to the head of a list
Returns

SinglyLinkedListNode pointer: a reference to the head of the merged list
Input Format

The first line contains an integer , the number of test cases.

The format for each test case is as follows:

The first line contains an integer , the length of the first linked list.
The next  lines contain an integer each, the elements of the linked list.
The next line contains an integer , the length of the second linked list.
The next  lines contain an integer each, the elements of the second linked list.

Constraints

, where  is the  element of the list.
Sample Input

1
3
1
2
3
2
3
4
Sample Output

1 2 3 3 4 
Explanation

The first linked list is: 

The second linked list is: 

Hence, the merged linked list is: """

class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def mergeList(head1 , head2):
    dummy = SinglyLinkedListNode(0)
    current = dummy
    while head1 and head2:
        if head1.data <= head2.data:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next
        
    current.next = head1 if head1 else head2
    return dummy.next
    
def buildList(arr):             
    if not arr:
        return None
    head = SinglyLinkedListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = SinglyLinkedListNode(val)
        current = current.next
    return head
    
result = mergeList(buildList([1,3,5]),
                   buildList([2,4,6]))  # ✅ convert first

while result:
    print(result.data, end=" ")
    result = result.next    
    