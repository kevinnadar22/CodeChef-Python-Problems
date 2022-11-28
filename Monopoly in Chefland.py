"""
https://www.codechef.com/problems/MONOPOLY

Problem

Chef is the financial incharge of Chefland and one of his duties is identifying if any company has gained a monopolistic advantage in the market.

There are exactly 3 companies in the market each of whose revenues are denoted by R1R1​, R2R2​ and R3R3​ respectively. A company is said to have a monopolistic advantage if its revenue is strictly greater than the sum of the revenues of its competitors.

Given the revenue of the 3 companies, help Chef determine if any of them has a monopolistic advantage.
Input Format

    The first line of input will contain a single integer T, denoting the number of test cases.
    Each test case consists of a single line of input containing three space separated integers R1R1​, R2R2​ and R3R3​ denoting the revenue of the three companies respectively.

Output Format

For each test case, output YESYES if any of the companies has a monopolistic advantage over its competitors, else output NONO.

You may print each character of the string in uppercase or lowercase (for example, the strings YeSYeS, yEsyEs, yesyes and YESYES will all be treated as identical).

Explanation:

Test case 1: All the companies have equal revenue so none have a monopolistic advantage.

Test case 2: The third company has a monopolistic advantage as 1+2<41+2<4.

Test case 3: The second company has a monopolistic advantage as 2+3<102+3<10."""


for _ in range(int(input())):
    r = sorted(map(int,input().split()))
    print("Yes" if r[0] + r[1] < r[2] else "No")