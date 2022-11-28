"""
https://www.codechef.com/problems/PRACLIST

Problem

CodeChef recently revamped its practice page to make it easier for users to identify the next problems they should solve by introducing some new features:

    Recent Contest Problems - contains only problems from the last 2 contests
    Separate Un-Attempted, Attempted, and All tabs
    Problem Difficulty Rating - the Recommended dropdown menu has various difficulty ranges so that you can attempt the problems most suited to your experience
    Popular Topics and Tags

Our Chef is currently practicing on CodeChef and is a beginner. The count of ‘All Problems’ in the Beginner section is XX. Our Chef has already ‘Attempted’ YY problems among them. How many problems are yet ‘Un-attempted’?
Input Format

    The first and only line of input contains two space-separated integers XX and YY — the count of 'All problems' in the Beginner's section and the count of Chef's 'Attempted' problems, respectively.

Output Format

Output a single integer in a single line — the number of problems that are yet 'Un-attempted'

Explanation:

Test case 11: There are 1010 problems in total in the Beginner's section, out of which 44 have been attempted. Hence, there are 66 Un-attempted problems.

Test case 22: There are 1010 problems in total in the Beginner's section, out of which all have been attempted. Hence, there are 00 Un-attempted problems.

Test case 33: There are 10001000 problems in total in the Beginner's section, out of which 990990 have been attempted. Hence, there are 1010 Un-attempted problems.

Test case 44: There are 500500 problems in total in the Beginner's section, out of which only 11 has been attempted. Hence, there are 499499 Un-attempted problems."""


x,y = map(int,input().split())
print(x-y)