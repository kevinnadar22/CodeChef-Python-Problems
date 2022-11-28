"https://www.codechef.com/problems/TAXES"

t=int(input())
for _ in range(t):
    revenue = int(input())
    tax = 10
    print(revenue - tax if revenue > 100 else revenue)