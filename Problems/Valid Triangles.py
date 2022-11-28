"https://www.codechef.com/LP0TO101/problems/FLOW013"

t=int(input())
for _ in range(t):
    theta = 180
    n = list(map(int, input().split()))
    print("YES" if sum(n)==theta else "NO")