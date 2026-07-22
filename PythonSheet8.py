# 1. Highest Profit Month
# Definition: Find the maximum value and its position while reading inputs.
# Task: A shop owner records the profit for N months. Print the highest profit and its month number.
# Example Input:
# 5
# 12000
# 15000
# 9800
# 17500
# 16000
# Example Output:
# Highest Profit = 17500
# Month = 4

n = int(input("Enter N: "))
month = 0
largest = 0
for i in range(1,n+1):
    num = int(input("Enter Profits: "))
    if num > largest:
        largest = num
        month = i
print("Highest Profit:",largest)
print("Month:",month)

# 2. Perfect Square Counter
# Definition: A perfect square is the square of an integer.
# Task: Read N numbers and count how many are perfect squares.
# Example Input:
# 5
# 16
# 20
# 25
# 18
# 49
# Example Output:
# 3

n = int(input("Enter N value: "))
count = 0
for i in range(n):
    num = int(input("Enter numbers: "))
    m = 1
    while m * m <= num:
        if m * m == num:
            count += 1
            break
        m+=1
print(count)


# 3. Sum of Multiples of 7
# Definition: Multiples of 7 are numbers divisible by 7.
# Task: Read A and B. Sum all multiples of 7 between them.
# Example Input:
# 10
# 35
# Example Output:
# 84

a = int(input("Enter A: "))
b = int(input("Enter B: "))
sum = 0
for i in range(a, b + 1):
    if i % 7 == 0:
        sum += i
print(sum)

# 4. Longest Positive Streak
# Definition: A streak is consecutive values satisfying a condition.
# Task: Read N numbers and find the longest positive streak.
# Example Input:
# 8
# 5
# 7
# -2
# 4
# 9
# 10
# 12
# -5
# Example Output:
# 4

n = int(input("Enter N: "))
current = 0
longest = 0
for i in range(n):
    num = int(input("Enter number: "))
    if num > 0:
        current += 1
        if current > longest:
            longest = current
    else:
        current = 0
print(longest)


# 5. Count Numbers with Exactly Three Divisors
# Definition: Some numbers have exactly three positive divisors.
# Task: Read N numbers and count them.
# Example Input:
# 5
# 4
# 9
# 8
# 16
# 25
# Example Output:
# 3

n = int(input("Enter N numbers: "))
count = 0
for i in range(1,n+1):
    num = int(input("Enter numbers: "))
    if num%i==0:
        count+=1
if count==3:
    print(count)
else:
    print("There is no positive divisors")

# 6. Largest Difference
# Definition: Difference is the gap between two values.
# Task: Find the largest difference between consecutive inputs.
# Example Input:
# 5
# 10
# 25
# 18
# 40
# 32
# Example Output:
# 22

n = int(input("Enter N: "))
prev = int(input("Enter number: "))
largest_diff = 0
for i in range(2, n + 1):
    curr = int(input("Enter number: "))
    diff = curr - prev
    if diff < 0:
        diff = -diff
    if diff > largest_diff:
        largest_diff = diff
    prev = curr
print("Largest Difference =", largest_diff)


# 7. Salary Bonus
# Definition: Employees below a threshold qualify.
# Task: Count salaries below Rs.30000.
# Example Input:
# 5
# 25000
# 40000
# 18000
# 32000
# 29000
# Example Output:
# 3

n = int(input("Enter N Employees: "))
count = 0
for i in range(1,n+1):
    sal = int(input("Enter Salaries: "))
    if sal < 30000:
        count+=1
print(count)


# 8. Largest Digit Sum
# Definition: Digit sum is the sum of all digits.
# Task: Print the number having the largest digit sum.
# Example Input:
# 4
# 123
# 98
# 555
# 71
# Example Output:
# 555

n = int(input("Enter N: "))
largest_sum = 0
largest_number = 0
for i in range(n):
    num = int(input("Enter number: "))
    temp = num
    digit_sum = 0
    while temp > 0:
        digit = temp % 10
        digit_sum += digit
        temp //= 10
    if digit_sum > largest_sum:
        largest_sum = digit_sum
        largest_number = num
print(largest_number)


# 9. Average Until Zero
# Definition: Average equals total divided by count.
# Task: Read numbers until 0 and print the average.
# Example Input:
# 8
# 12
# 20
# 0
# Example Output:
# 13.33

sum = 0
count = 0
while True:
    num = int(input("Enter Numbers: "))
    if num==0:
        break
    count+=1
    sum+=num
    average = sum / count
print(average)


# 10. Count Numbers Greater Than Average
# Definition: Compare values with the calculated average.
# Task: Read N numbers, compute average, then count numbers above it.
# Example Input:
# 5
# 10
# 20
# 30
# 40
# 50
# Example Output:
# 2

n = int(input("Enter N: "))
numbers = [0] * n
sum = 0
for i in range(n):
    numbers[i] = int(input("Enter number: "))
    sum += numbers[i]
average = sum / n
count = 0
for i in range(n):
    if numbers[i] > average:
        count += 1
print(count)

