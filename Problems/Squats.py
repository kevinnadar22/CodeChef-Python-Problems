"""
https://www.codechef.com/problems/SQUATS

Problem

Somu went to the gym today. He decided to do X sets of squats. Each set consists of 1515 squats. Determine the total number of squats that he did today.
Input Format

    The first line contains a single integer T — the number of test cases. Then the test cases follow.
    The first and only line of each test case contains an integer X — the total number of sets of squats that Somu did.

Output Format

For each test case, output the total number of squats done by Somu.

Explanation:

Test Case 1: Since, he does only 11 set of squats, the total number of squats done by him is 1515.

Test Case 2: Since, he does 44 sets of squats, the total number of squats is 15+15+15+15=6015+15+15+15=60.

"""


t=int(input())
for _ in range(t):
    reps = 15
    sets = int(input())
    print(reps*sets)
