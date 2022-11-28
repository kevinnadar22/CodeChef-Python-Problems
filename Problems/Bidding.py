"https://www.codechef.com/problems/AUCTION"

t=int(input())
for _ in range(t):
    a,b,c=map(int, input().split())
    bid = max(a,b,c)
    info = {a: "alice", b:"bob", c: "charlie"}
    print(info[bid])