# 1. Consecutive Pass Count
# Definition: A consecutive pass means students pass one after another without any failure in
# between.
# Task: Read marks of N students and find the longest consecutive sequence of students scoring 35
# or more.
# Example Input:
# 8
# 40
# 55
# 20
# 36
# 70
# 90
# 15
# 45
# Example Output:
# Longest Consecutive Passes = 3

n=int(input("Enter N value: "))
count = 0
longest = 0
for i in range(n):
    num = int(input("Enter numbers: "))
    if num >= 35:
        count+=1
        if count > longest:
            longest = count
    else:
        count = 0
print("Longest Consecutive Passes ", longest)


# 2. Largest Prime Entered
# Definition: A prime number has exactly two positive divisors.
# Task: Read N numbers and print the largest prime.
# Example Input:
# 6
# 12
# 17
# 21
# 29
# 18
# 7
# Example Output:
# Largest Prime = 29

n=int(input("Enter N value: "))
largest = 0
count = 0
m = 1
for i in range(n):
    num = int(input("Enter numbers: "))
    count = 0
    m = 1
    while m <= num:
        if num%m==0:
            count+=1
        m+=1
    if count == 2:
        if num > largest:
            largest = num
print("Largest Prime",largest)




# 3. Sum of Even Digits
# Definition: Even digits are 0,2,4,6,8.
# Task: Read a number and print the sum of even digits.
# Example Input:
# 4827316
# Example Output:
# 20

nums = int(input("Enter number: "))
sum = 0
while nums > 0:
    digit = nums % 10
    if digit % 2 == 0:
        sum += digit
    nums //= 10
print(sum)


# 4. Factory Quality Check
# Definition: Quality below 50 is defective.
# Task: Read N scores and print defective and good counts.
# Example Input:
# 6
# 45
# 60
# 72
# 38
# 80
# 49
# Example Output:
# Defective = 3
# Good = 3

n = int(input("Enter N value: "))
defective_count = 0
good_count = 0
for i in range(1,n+1):
    num = int(input("Enter Numbers: "))
    if num > 50:
        defective_count+=1
    else:
        good_count+=1
print("Defective:",defective_count)
print("Good:",good_count)


# 5. Maximum Sales Increase
# Definition: Increase is today's sales minus yesterday's.
# Task: Find the maximum increase between consecutive days.
# Example Input:
# 5
# 100
# 130
# 110
# 180
# 200
# Example Output:
# Maximum Increase = 70

n = int(input("Enter N value: "))
previous = int(input("Enter Sales: "))
max_increase = 0
for i in range(1, n):
    current = int(input("Enter Sales: "))
    increase = current - previous
    if increase > max_increase:
        max_increase = increase
    previous = current
print("Maximum Increase =", max_increase)



# 6. Number with Most Digits
# Definition: Digit count is the number of digits.
# Task: Print the number with the most digits.
# Example Input:
# 5
# 23
# 9876
# 105
# 123456
# 89
# Example Output:
# 123456

n = int(input("Enter N value: "))
digits = 0
max_num = 0
for i in range(n):
    num = int(input("Enter Number: "))
    temp = num
    count = 0
    if temp == 0:
        count = 1
    else:
        while temp > 0:
            count += 1
            temp //= 10
    if count > digits:
        digits = count
        max_num = num
print(max_num)

# 7. Count Numbers Divisible by Both 4 and 6
# Definition: Such numbers are divisible by 12.
# Task: Count such numbers.
# Example Input:
# 6
# 12
# 24
# 18
# 36
# 40
# 48
# Example Output:
# 4

n = int(input("Enter N value: "))
count = 0
for i in range(n):
    num = int(input("Enter numbers: "))
    if num%4==0 and num%6==0:
        count+=1
print(count)

# 8. Longest Odd Streak
# Definition: An odd streak is consecutive odd numbers.
# Task: Find the longest odd streak.
# Example Input:
# 8
# 3
# 5
# 8
# 7
# 9
# 11
# 4
# 13
# Example Output:
# 3

n = int(input("Enter N value: "))
count = 0
max_count = 0
for i in range(n):
    num = int(input("Enter Number: "))
    if num % 2 != 0:
        count += 1
        if count > max_count:
            max_count = count
    else:
        count = 0
print(max_count)


# 10. Running Balance
# Definition: Running balance updates after each transaction.
# Task: Print balance after each transaction and final balance.
# Example Input:
# 1000
# 4
# 500
# -200
# 300
# -100
# Example Output:
# Balance=1500
# Balance=1300
# Balance=1600
# Balance=1500
# Final Balance=1500

bal = int(input("Enter Balanace: "))
n = int(input("Enter n transactions: "))
for i in range(n):
    num = int(input("Enter amount: "))
    bal+=num
    print("Balance",bal)
print("Final Balance",bal)



