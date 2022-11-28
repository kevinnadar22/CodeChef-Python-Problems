n = int(input())
remainder = lambda x: print(int(x[0]) % int(x[1]))
i = [remainder(input().split()) for _ in range(n)]

"https://www.codechef.com/LP0TO101/problems/FLOW002"