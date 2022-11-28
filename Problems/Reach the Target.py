"https://www.codechef.com/problems/REACHTARGET"

t = int(input())

for _ in range(t):
    x,y = map(int, input().split())
    print(max(x-y, 0))