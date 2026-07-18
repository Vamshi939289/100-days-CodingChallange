# 1. Count Even and Odd Numbers from 1 to N
# Problem Definition: A program can classify numbers as even or odd.
# Task: Read N. Count even and odd numbers from 1 to N.
# Example Input:
# 10
# Example Output:
# Even Numbers = 5
# Odd Numbers = 5

n = int(input("Enter N value: "))
even = 0
odd = 0
count = 1
for i in range(1,n+1):
    if i%2==0:
        even+=1
    else:
        odd+=1
    count+=1
print("Even Numbers: ",even)
print("Odd Numbers: ",odd)


# 2. Sum of Numbers Divisible by 3
# Problem Definition: Process only numbers that satisfy a condition.
# Task: Read N. Find the sum of numbers divisible by 3.
# Example Input:
# 10
# Example Output:
# 18

n = int(input("Enter N value: "))
sum = 0
count = 1
for i in range(1,n+1):
    if i%3==0:
        sum+=i
    count+=1
print("Sum of numbers:",sum)



# 3. Print Leap Years in a Range
# Problem Definition: Leap years follow specific rules.
# Task: Read start year and end year. Print all leap years.
# Example Input:
# 2000
# 2020


start = 2000
end = 2020
while start <= end:
    if (start%400 == 0 or (start%4==0 and start%100 != 0)):
        print(start)
    start+=1





# 4. Count Multiples of 5 and 7
# Problem Definition: Numbers may satisfy multiple divisibility rules.
# Task: Read N. Count multiples of 5, 7 and both.
# Example Input:
# 50
# Example Output:
# 5=10
# 7=7
# Both=1

n = int(input("Enter Value of N: "))
five_mul = 0
seven_mul = 0
both_mul = 0
while n > 0:
    if n%5==0:
        five_mul+=1
    if n%7==0:
        seven_mul+=1
    if (n%5==0 and n%7==0):
        both_mul+=1
    n-=1
print("5:",five_mul)
print("7:",seven_mul)
print("Both:",both_mul)

# 5. Print All Factors and Their Count
# Problem Definition: Factors divide a number exactly.
# Task: Print all factors and total count.
# Example Input:
# 12
# Example Output:
# 1 2 3 4 6 12
# Total Factors = 6

num = int(input("Enter Number: "))
count = 0
fact = 1
n=num
while num > 0 and fact<=n:
    if n%fact==0:
        print(fact,end=" ")
        count+=1
    num-=1
    fact+=1
print()
print("Total Factors: ",count)


# 6. Largest Digit
# Problem Definition: Find the greatest digit.
# Task: Read a number and print the largest digit.
# Example Input:
# 583920
# Example Output:
# Largest Digit = 9

num = int(input("Enter a Number: "))
largest = 0
while num > 0:
    digit = num % 10
    if digit > largest:
        largest = digit
    num //=10
print("Largest Digit:",largest)

# 7. Smallest Digit
# Problem Definition: Find the smallest digit.
# Task: Read a number and print the smallest digit.
# Example Input:
# 583920
# Example Output:
# Smallest Digit = 0

num = int(input("Enter a Number: "))
smallest = 0
while num > 0:
    digit = num % 10
    if digit < smallest:
        smallest = digit
    num //=10
print("Smallest Digit:",smallest)

# 8. Count Digits Greater Than 5
# Problem Definition: Count digits meeting a condition.
# Task: Read a number and count digits > 5.
# Example Input:
# 589762
# Example Output:
# 4


num = int(input("Enter a Number: "))
count=0
while num > 0:
    digit = num % 10
    if digit > 5:
        count+=1
    num //=10
print("Digits Greater than 5: ",count)

# 9. Sum Only Even Digits
# Problem Definition: Add only even digits.
# Task: Read a number and print the sum of even digits.
# Example Input:
# 58294
# Example Output:
# 14


num = int(input("Enter a Number: "))
count=0
while num > 0:
    digit = num % 10
    if digit%2==0:
        count+=digit
    num //=10
print("Sum of even digits: ",count)

# 10. Divisible by 3 but Not 5
# Problem Definition: Filter numbers using two conditions.
# Task: Read N and print numbers divisible by 3 but not 5.
# Example Input:
# 30
# Example Output:
# 3 6 9 12 18 21 24 27


num = int(input("Enter a Number: "))
n=1
while n<=num:
    if n%3 == 0 and n%5 != 0:
        print(n,end=" ")
    n+=1



