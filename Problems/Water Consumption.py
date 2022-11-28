"""
https://www.codechef.com/problems/WATERCONS

Problem

Recently, Chef visited his doctor. The doctor advised Chef to drink at least 20002000 ml of water each day.

Chef drank X ml of water today. Determine if Chef followed the doctor's advice or not.
Input Format

    The first line contains a single integer T — the number of test cases. Then the test cases follow.
    The first and only line of each test case contains one integer X — the amount of water Chef drank today.

Output Format

For each test case, output YES if Chef followed the doctor's advice of drinking at least 20002000 ml of water. Otherwise, output NO.

You may print each character of the string in uppercase or lowercase (for example, the strings YES, yEs, yes, and yeS will all be treated as identical).

Test case 11: Chef followed the doctor's advice since he drank 29992999 ml of water which is ≥2000≥2000 ml.

Test case 22: Chef did not follow the doctor's advice since he drank 14501450 ml of water which is <2000<2000 ml.

Test case 33: Chef followed the doctor's advice since he drank 20002000 ml of water which is ≥2000≥2000 ml"""

t=int(input())

for _ in range(t):
    print("yes" if int(input()) >= 2000 else "no")