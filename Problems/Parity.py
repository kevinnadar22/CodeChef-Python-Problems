"""
https://www.codechef.com/problems/PAR2

Problem

Ashu and Arvind participated in a coding contest, as a result of which they received N chocolates. Now they want to divide the chocolates between them equally.

Can you help them by deciding if it is possible for them to divide all the N chocolates in such a way that they each get an equal number of chocolates?

You cannot break a chocolate in two or more pieces.
Input Format

    The first line of input will contain a single integer T, denoting the number of test cases.
    The first and only line of each test case contains a single integer N — the number of chocolates they received.

Output Format

For each test case output the answer on a new line — "Yes" (without quotes) if they can divide chocolates between them equally, and "No" (without quotes) otherwise.

Each letter of the output may be printed in either uppercase or lowercase, i.e, "Yes", "YES", and "yEs" will all be treated as equivalent.

Explanation:

Test case 11: They can divide 1010 chocolates such that both of them get 55 chocolates each.

Test case 22: They can divide 44 chocolates such that both of them get 22 chocolates each.

Test case 33: There is no way to divide 33 chocolates so that they get equal number of chocolates.

Test case 44: They can divide 22 chocolates such that both of them get 11 chocolate each.
"""

for _ in range(int(input())):
    print("yes" if int(input())%2==0 else "no")