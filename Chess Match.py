"https://www.codechef.com/problems/BLITZ3_2"

t=int(input())
sec = 180
for _ in range(t):
    n, a, b = map(int, input().split())
    print(2*(sec+n)-(a+b))
