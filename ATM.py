"https://www.codechef.com/LP0TO101/problems/HS08TEST"


tax = 0.50
multiple=5
num = input().split()
x,y = int(num[0]), float(num[1])
print(y if x % multiple != 0 or x+tax>y else y-x-tax)