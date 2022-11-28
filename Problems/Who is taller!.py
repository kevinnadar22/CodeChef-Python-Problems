"https://www.codechef.com/problems/TALLER"

t = int(input())

for _ in range(t):
    a,b = map(int, input().split())
    print("A" if a>b else "B")



