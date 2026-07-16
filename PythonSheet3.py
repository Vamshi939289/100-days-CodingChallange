# 1. Find the Largest of N Numbers
# Problem Definition: Find the greatest value from a sequence of numbers.
# Task: Read N, then read N numbers one by one and print the largest.
# Example Input:
# N=5
# 12
# 45
# 8
# 90
# 34
# Example Output:
# Largest = 90

def largest():
    n = int(input("Enter the value of N: "))
    count = 1
    largest = int(input("Enter number 1: "))
    while count < n:
        num = int(input(f"Enter number {count + 1}: "))
        if num > largest:
            largest = num
        count += 1
    print("Largest =", largest)
largest()

# 2. Find the Smallest of N Numbers
# Problem Definition: Find the smallest value from a sequence of numbers.
# Task: Read N numbers and print the smallest.
# Example Input:
# N=5
# 18
# 3
# 45
# 7
# 12
# Example Output:
# Smallest = 3

def smallest():
    n = int(input("Enter the value of N: "))
    count = 1
    smallest = int(input("Enter number 1: "))
    while count < n:
        num = int(input(f"Enter number {count + 1}: "))
        if num < smallest:
            smallest = num
        count+=1
    print("Smallest:", smallest)
smallest()

# 3. Find the Second Largest Number
# Problem Definition: Find the second highest value without sorting.
# Task: Read N numbers and print the second largest.
# Example Input:
# N=5
# 25
# 60
# 15
# 80
# 50
# Example Output:
# Second Largest = 60


def secondlargest():
    n = int(input("Enter the value of N: "))
    count = 1
    largest = int(input("Enter number 1: "))
    secondlargest = 0
    while count < n:
        num = int(input(f"Enter number {count + 1}: "))
        if num > largest:
            secondlargest = largest
            largest = num
        elif num > secondlargest and num!=largest:
            secondlargest = num
        count += 1
    print("Second Largest:", secondlargest)
secondlargest()


# 4. Find the Second Smallest Number
# Problem Definition: Find the second lowest value without sorting.
# Task: Read N numbers and print the second smallest.
# Example Input:
# N=5
# 25
# 60
# 15
# 80
# 50
# Example Output:
# Second Smallest = 25

def secondsmallest():
    n = int(input("Enter the value N: "))
    count = 1
    smallest = int(input("Enter number 1: "))
    secondsmallest = 0
    while count < n:
        num = int(input(f"Enter number {count + 1}: "))
        if num < smallest:
            secondsmallest = smallest
            smallest = num
        elif num < secondsmallest and num != smallest:
            secondsmallest = num
        count+=1
    print("Second smallest: ", secondsmallest)
secondsmallest()

# 5. Count Positive, Negative and Zero Values
# Problem Definition: Classify numbers based on their sign.
# Task: Read N numbers and count positives, negatives and zeros.
# Example Input:
# N=6
# 10
# -5
# 0
# 18
# -2
# 0
# Example Output:
# Positive = 2
# Negative = 2
# Zero = 2

def classifynumbers():
    n = int(input("Enter the value N: "))
    count = 1
    positive_count = 0
    negative_count = 0
    zero = 0
    num = int(input("Enter number 1: "))
    if num > 0:
        positive_count+=1
    elif num < 0:
        negative_count+=1
    else:
        zero+=1
    while count < n:
        num = int(input(f"Enter number {count + 1}: "))
        if num > 0:
            positive_count+=1
        elif num < 0:
            negative_count+=1
        else:
            zero+=1
        count+=1
    print("Positive:", positive_count)
    print("Negative:", negative_count)
    print("Zero:", zero)
classifynumbers()


# 6. Find the Missing Number
# Problem Definition: One number from 1 to N is missing.
# Task: Read N and the remaining numbers, then find the missing number.
# Example Input:
# N=6
# 1
# 2
# 3
# 5
# 6
# Example Output:
# Missing Number = 4

def missing():
    n = int(input("Enter the value N: "))
    expected_sum = 0
    actual_sum = 0
    count = 1
    while count <= n:
        expected_sum += count
        count+=1
    count = 1
    while count < n:
        num = int(input(f"Enter number {count}: "))
        actual_sum+=num
        count+=1
    missing = expected_sum - actual_sum
    print("Missing Number:",missing)
missing()

# 7. Check Whether a Number is Perfect
# Problem Definition: A perfect number equals the sum of its proper factors.
# Task: Determine whether the given number is perfect.
# Example Input:
# 28
# Example Output:
# Perfect Number

def perfectnumber():
    num = int(input("Enter a number: "))
    count = 1
    total = 0
    while count < num:
        if num % count == 0:
            total += count
        count += 1
    if total == num:
        print("Perfect Number")
    else:
        print("Not a Perfect Number")
perfectnumber()

# 8. Find the GCD of Two Numbers
# Problem Definition: The GCD is the greatest number that divides both numbers.
# Task: Find the GCD using loops.
# Example Input:
# 24
# 36
# Example Output:
# GCD = 12

def gcd():
    n1 = int(input("Enter number 1: "))
    n2 = int(input("Enter number 2: "))
    count = 1
    gcd = 1
    while count<=n1 and count<=n2:
        if n1%count == 0 and n2%count == 0:
            gcd = count
        count+=1
    print("GCD:",gcd)
gcd()

# 10. Power Without Using **
# Problem Definition: Calculate a power using repeated multiplication.
# Task: Read the base and exponent, then compute the result using a loop.
# Example Input:
# Base = 3
# Exponent = 4
# Example Output:
# 81

def power():
    base = int(input("Enter Base: "))
    exponent = int(input("Enter Exponent: "))
    count = 1
    result = 1
    while count <= exponent:
        result = result * base
        count+=1
    print("Result:",result)
power()






