"""
https://www.codechef.com/problems/AGELIMIT

Problem

Chef wants to appear in a competitive exam. To take the exam, there are following requirements:

    Minimum age limit is X (i.e. Age should be greater than or equal to X).
    Age should be strictly less than Y.

Chef's current Age is AA. Find whether he is currently eligible to take the exam or not.
Input Format

    First line will contain T, number of test cases. Then the test cases follow.
    Each test case consists of a single line of input, containing three integers X,Y,X,Y, and AA as mentioned in the statement.

Output Format

For each test case, output YES if Chef is eligible to give the exam, NO otherwise.

You may print each character of the string in uppercase or lowercase (for example, the strings YES, yEs, yes, and yeS will all be treated as identical).

Explanation:

Test case 11: The age of Chef is 3030. His age satisfies the minimum age limit as 30≥2130≥21. Also, it is less than the upper limit as 30<3430<34. Thus, Chef is eligible to take the exam.

Test case 22: The age of Chef is 3131. His age satisfies the minimum age limit as 31≥2531≥25. But, it is not less than the upper limit as 31≮3131≮31. Thus, Chef is not eligible to take the exam.

Test case 33: The age of Chef is 2525. His age satisfies the minimum age limit as 25≥2225≥22. Also, it is less than the upper limit as 25<2925<29. Thus, Chef is eligible to take the exam.

Test case 44: The age of Chef is 1515. His age does not satisfy the minimum age limit as 15<2015<20. Thus, Chef is not eligible to take the exam."""

t=int(input())

for _ in range(t):
    X,Y,A=map(int,input().split())
    print("yes" if A>=X and A<Y else "no")