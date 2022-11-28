"""
https://www.codechef.com/problems/BESTOFTWO

Problem

Chef took an examination two times. In the first attempt, he scored XX marks while in the second attempt he scored YY marks. According to the rules of the examination, the best score out of the two attempts will be considered as the final score.

Determine the final score of the Chef.
Input Format

    The first line contains a single integer TT — the number of test cases. Then the test cases follow.
    The first line of each test case contains two integers XX and YY — the marks scored by Chef in the first attempt and second attempt respectively.

Output Format

For each test case, output the final score of Chef in the examination.

Explanation:

Test Case 1: The best score out of the two attempts is 6060.

Test Case 2: The best score out of the two attempts is 6767.

Test Case 3: The best score out of the two attempts is 5050.
"""

t=int(input())

for _ in range(t):
    x,y=input().split()
    print(max(int(x), int(y)))