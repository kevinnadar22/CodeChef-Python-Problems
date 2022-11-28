"https://www.codechef.com/problems/PRIMEDICE"

t=int(input())

inf= {"A":"Alice", "B":"Bob"}

for _ in range(t):
    bob_won = False
    x,y=map(int,input().split())
    n = sum([x,y])
    for i in range(2,10):
        pr_n = n/i if n!=i else 1.5
        if pr_n.is_integer():
            bob_won = True
            print(inf["B"])
            break

    None if bob_won else print(inf["A"])
