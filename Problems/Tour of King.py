"https://www.codechef.com/problems/KNGTOR"

# cook your dish here
for _ in range(int(input())):
    # Read the values of n5 and n7 from the input
    n5, n7 = map(int, input().split())
    
    # Calculate the total number of seats available in the 5-seater cars and the 7-seater cars
    total_seats_5 = 5 * n5
    total_seats_7 = 7 * n7
    
    # Find the minimum of the total number of seats available in the 5-seater cars and the 7-seater cars
    max_people = total_seats_5 + total_seats_7
    
    # Output the result
    print(max_people)
