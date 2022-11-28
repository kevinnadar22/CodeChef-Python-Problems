"https://www.codechef.com/problems/ADVANCE"

t=int(input())

for _ in range(t):
    x,y = map(int, input().split())
    n_list = list(range(x, x+200+1))
    print("No" if y not in n_list else "Yes")