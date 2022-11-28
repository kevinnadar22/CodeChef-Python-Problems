"https://www.codechef.com/LP0TO101/problems/LUCKFOUR"

t=int(input())
k=4
for _ in range(t):
    n = list(map(int, list(input())))
    print(n.count(k))