"https://www.codechef.com/LP0TO101/problems/INTEST"


n, k = map(int, input().split())
c = sum(1 if int(input())%k == 0 else 0 for _ in range(n))
print(c)