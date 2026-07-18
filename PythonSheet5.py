# Day 5 - Logic Building (Loops + Conditions)
# 1. Print Numbers Divisible by Both 3 and 5
# Problem Definition: Some numbers satisfy multiple conditions at the same time.
# Task: Read N and print all numbers from 1 to N divisible by both 3 and 5.
# Example Input:
# 50
# Example Output:
# 15
# 30
# 45

num = int(input("Enter a number: "))
n = 1
while n <= num:
    if n%3==0 and n%5==0:
        print(n)
    n+=1

# 2. Count Numbers Ending with 5
# Problem Definition: The last digit helps identify patterns.
# Task: Read N and count numbers from 1 to N ending with 5.
# Example Input:
# 35
# Example Output:
# 4

num = int(input("Enter Number: "))
n = 1
count = 0
while n <= num:
    if n%10 == 5:
        count+=1
    n+=1
print(count)

# 3. Sum Numbers Whose Last Digit is Even
# Problem Definition: Check only the last digit before adding.
# Task: Read N and find the sum of numbers whose last digit is even.
# Example Input:
# 10
# Example Output:
# 30

num = int(input("Enter Number: "))
n = 1
count = 0
while n <= num:
    digit = n % 10
    if digit % 2 == 0:
        count+=n
    n+=1
print(count)

# 4. Print Numbers Whose Square is Less Than N
# Problem Definition: Print numbers only if their square is less than N.
# Task: Read N and print such numbers.
# Example Input:
# 30
# Example Output:
# 1
# 2
# 3
# 4
# 5

num = int(input("Enter Number: "))
n = 1
while n * n < num:
    print(n)
    n+=1

# 5. Count Numbers Divisible by 4 but Not by 6
# Problem Definition: Combine two divisibility conditions.
# Task: Read N and count numbers divisible by 4 but not 6.
# Example Input:
# 30
# Example Output:
# 6

num = int(input("Enter Number: "))
n = 1
count=0
while n <= num:
    if n%4==0 and n%6 != 0:
        count+=1
    n+=1
print(count)

# 7. First Number Divisible by Both 7 and 9
# Problem Definition: Stop when the required number is found.
# Task: Read N and print the first number greater than N divisible by both 7 and 9.
# Example Input:
# 50
# Example Output:
# 63

num = int(input("Enter Number: "))
n = num + 1
while True:
    if n % 7 == 0 and n % 9 == 0:
        print(n)
        break
    n += 1

# 9. Print Factors Greater Than 5
# Problem Definition: Filter factors using a condition.
# Task: Read a number and print only factors greater than 5.
# Example Input:
# 60
# Example Output:
# 6
# 10
# 12
# 15
# 20
# 30

num = int(input("Enter number: "))
n = 1
while n <= num:
    if num%n == 0 and n > 5 :
        print(n)
    n+=1


# 10. Sum Until a Negative Number Appears
# Problem Definition: Use a negative number as the stopping condition.
# Task: Read numbers until a negative appears and print the sum.
# Example Input:
# 10
# 20
# 15
# 8
# -1
# Example Output:
# 53

sum = 0
while True:
    num = int(input())
    if num < 0:
        break
    sum += num
print("Sum =", sum)