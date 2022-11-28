"https://www.codechef.com/LP0TO101/problems/CHOPRT"

t=int(input())
func1 = lambda x,y: ">" if x>y else "<"
func2 = lambda x,y: "=" if x==y else func1(x,y)
for _ in range(t):
    x,y=map(int, input().split())
    print(func2(x,y))