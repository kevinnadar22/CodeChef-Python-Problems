"https://www.codechef.com/LP0TO101/problems/FLOW007"

t=int(input())
for _ in range(t):
    n=map(int, list(input()))
    n.reverse()
    print(int("".join(n)))