"https://www.codechef.com/problems/AUDIBLE"

for _ in range(int(input())):
    hertz = int(input())
    print("YES" if 67 <= hertz <= 45000 else "NO")