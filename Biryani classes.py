"""
https://www.codechef.com/problems/BIRYANI

Problem

According to a recent survey, Biryani is the most ordered food. Chef wants to learn how to make world-class Biryani from a MasterChef. Chef will be required to attend the MasterChef's classes for X weeks, and the cost of classes per week is Y coins. What is the total amount of money that Chef will have to pay?
Input Format

    The first line of input will contain an integer T — the number of test cases. The description of T test cases follows.
    The first and only line of each test case contains two space-separated integers X and Y, as described in the problem statement.

Output Format

For each test case, output on a new line the total amount of money that Chef will have to pay.

Explanation:

Test case 11: Chef will be required to attend the MasterChef's classes for 11 week and the cost of classes per week is 1010 coins. Hence, Chef will have to pay 1010 coins in total.

Test case 22: Chef will be required to attend the MasterChef's classes for 11 week and the cost of classes per week is 1515 coins. Hence, Chef will have to pay 1515 coins in total.

Test case 33: Chef will be required to attend the MasterChef's classes for 22 weeks and the cost of classes per week is 1010 coins. Hence, Chef will have to pay 2020 coins in total.

Test case 44: Chef will be required to attend the MasterChef's classes for 22 weeks and the cost of classes per week is 1515 coins. Hence, Chef will have to pay 3030 coins in total."""

t=int(input())

for _ in range(t):
    x,y=map(int, input().split())
    print(x*y)