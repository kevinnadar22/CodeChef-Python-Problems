"""
https://www.codechef.com/problems/FIT

Problem

Chef wants to become fit for which he decided to walk to the office and return home by walking. It is known that Chef's office is X km away from his home.

If his office is open on 55 days in a week, find the number of kilometers Chef travels through office trips in a week.
Input Format

    First line will contain T, number of test cases. Then the test cases follow.
    Each test case contains of a single line consisting of single integer X.

Output Format

For each test case, output the number of kilometers Chef travels through office trips in a week.

Explanation:

Test case 11: The office is 11 km away. Thus, to go to the office and come back home, Chef has to walk 22 kms in a day. In a week with 55 working days, Chef has to travel 2⋅5=102⋅5=10 kms in total.

Test case 22: The office is 33 kms away. Thus, to go to the office and come back home, Chef has to walk 66 kms in a day. In a week with 55 working days, Chef has to travel 6⋅5=306⋅5=30 kms in total.

Test case 33: The office is 77 kms away. Thus, to go to the office and come back home, Chef has to walk 1414 kms in a day. In a week with 55 working days, Chef has to travel 14⋅5=7014⋅5=70 kms in total.

Test case 44: The office is 1010 kms away. Thus, to go to the office and come back home, Chef has to walk 2020 kms in a day. In a week with 55 working days, Chef has to travel 20⋅5=10020⋅5=100 kms in total."""

t=int(input())
for _ in range(t):
    print(int(input())*5*2)