"https://www.codechef.com/LP0TO101/problems/FLOW010"

t=int(input())
info = {"b" : "BattleShip", "c" : "Cruiser", "d" : "Destroyer","f":"Destroyer"}
for _ in range(t):
    raw_input = input().lower()
    print(info[raw_input])