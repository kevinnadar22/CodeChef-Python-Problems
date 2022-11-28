"""
https://www.codechef.com/problems/DETSCORE

Problem

Chef appeared for a placement test.

There is a problem worth XX points. Chef finds out that the problem has exactly 1010 test cases. It is known that each test case is worth the same number of points.

Chef passes NN test cases among them. Determine the score Chef will get.

NOTE: See sample explanation for more clarity.
Input Format

    First line will contain TT, number of test cases. Then the test cases follow.
    Each test case contains of a single line of input, two integers XX and NN, the total points for the problem and the number of test cases which pass for Chef's solution.

Output Format

For each test case, output the points scored by Chef.

Explanation:

Test Case 11: The problem is worth 1010 points and since there are 1010 test cases, each test case is worth 11 point. Since Chef passes 33 test cases, his score will be 1⋅3=31⋅3=3 points.

Test Case 22: The problem is worth 100100 points and since there are 1010 test cases, each test case is worth 1010 points. Since Chef passes all the 1010 test cases, his score will be 10⋅10=10010⋅10=100 points.

Test Case 33: The problem is worth 130130 points and since there are 1010 test cases, each test case is worth 1313 points. Since Chef passes 44 test cases, his score will be 13⋅4=5213⋅4=52 points.

Test Case 44: The problem is worth 7070 points and since there are 1010 test cases, each test case is worth 77 points. Since Chef passes 00 test cases, his score will be 7⋅0=07⋅0=0 points.
"""

t=int(input())
for _ in range(t):
    x,n=map(int, input().split())
    print(int((x/10)*n))