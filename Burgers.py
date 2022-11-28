"""
https://www.codechef.com/problems/BURGERS

Problem

Chef is fond of burgers and decided to make as many burgers as possible.

Chef has A patties and B buns. To make 11 burger, Chef needs 11 patty and 11 bun.
Find the maximum number of burgers that Chef can make.
Input Format

    The first line of input will contain an integer T — the number of test cases. The description of T test cases follows.
    The first and only line of each test case contains two space-separated integers AA and BB, the number of patties and buns respectively.

Output Format

For each test case, output the maximum number of burgers that Chef can make.

Explanation:

Test case 11: Chef has 22 patties and 22 buns, and therefore Chef can make 22 burgers.

Test case 22: Chef has 22 patties and 33 buns. Chef can make at most 22 burgers by using 22 patties and 22 buns.

Test case 33: Chef has 33 patties and 22 buns. Chef can make at most 22 burgers by using 22 patties and 22 buns.

Test case 44: Chef has 2323 patties and 1717 buns. Chef can make at most 1717 burgers by using 1717 patties and 1717 buns."""

t=int(input())

for _ in range(t):
    x,y = map(int, input().split())
    print(min(x,y))