""" Task

Students of District College have a subscription to English and French newspapers. Some students have subscribed to only the English newspaper, some have subscribed to only the French newspaper, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to only English newspapers.

Input Format

The first line contains the number of students who have subscribed to the English newspaper.
The second line contains the space separated list of student roll numbers who have subscribed to the English newspaper.
The third line contains the number of students who have subscribed to the French newspaper.
The fourth line contains the space separated list of student roll numbers who have subscribed to the French newspaper.

Constraints


Output Format

Output the total number of students who are subscribed to the English newspaper only.

Sample Input

9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
Sample Output

4
"""

def find_subscriptions(n,n1,n2,n3):
    n = int(input())
    n1 = set(map(int,input().split()))
    n3 = int(input())
    n4 = set(map(int,input().split()))
    
    e_subscription = []
    f_subscription = []
    for i in n1:
        if i not in n4:
            e_subscription.append(i)
        else:
            f_subscription.append(i)
    print(len(e_subscription))
    
find_subscriptions(0,0,0,0)