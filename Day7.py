# # Basic Unique Number Problems in Python
# # 1. Sum of First and Last Digit
# # Task: Given a number, find the sum of its first digit and last digit.
# # Example Input: Number = 58392
# # Example Output: First digit = 5, Last digit = 2, Sum = 7

def sumlastfirstdigit(num):
    last = num % 10
    while num>=10:
        num//=10
        first = num
    return last+first
print(f'The sum of last digit and first digit is : {sumlastfirstdigit(58392)}')


# # 2. Count Digits Greater Than 5
# # Task: Count digits in a number that are greater than 5.
# # Example Input: Number = 836921
# # Example Output: Digits greater than 5 = 4

def countdigits(n):
    count = 0
    while n>0:
        num = n % 10
        if num > 5:
            count+=1
        n //= 10
    return count
print(f'In the given number,the digits greater than 5 is:{countdigits(836921)}')

# # 3. Product of Digits at Odd Positions
# # Task: Find product of digits present at odd positions from right side.
# # Example Input: Number = 58294
# # Example Output: Product = 64

def digitsatoddposition(num):
    product = 1
    count = 0
    while num > 0:
        digit = num % 10
        count+=1
        if count%2 != 0:
            product *= digit
        num //= 10
    return product
print(f'Digit at odd positions:{digitsatoddposition(58294)}')

# # 4. Largest Digit Difference
# # Task: Find difference between largest and smallest digit.
# # Example Input: Number = 58392
# # Example Output: Largest = 9, Smallest = 2, Difference = 7

def largestdiff(num):
    largest = 0
    smallest = 2
    while num>0:
        digit = num % 10
        if digit > largest:
            largest = digit
        if digit < smallest:
            smallest = digit
        num //= 10
    return largest - smallest
print("Difference:", largestdiff(58392))

# # 5. Count Even and Odd Digits
# # Task: Count even and odd digits in a number.
# # Example Input: Number = 58392
# # Example Output: Even digits = 2, Odd digits = 3

def countevenodd(num):
    even_count = 0
    odd_count = 0
    while num > 0:
        if num%2 == 0:
            even_count+=1
        else:
            odd_count+=1
        num //= 10
    return even_count,odd_count
print(countevenodd(58392))

# 6. Reverse Number Without Changing Middle Digit
# Task: Reverse first and last digits while keeping middle digits unchanged.
# Example Input: Number = 12345
# Example Output: Result = 52341

def reversefirstlast(num):
    last = num % 10
    first = num
    p = 1
    while first >= 10:
        first //= 10
        p *= 10
    middle = (num % p) // 10
    return last * p + middle * 10 + first
print(reversefirstlast(12345))

# 7. Digit Sum Until Single Digit
# Task: Add digits repeatedly until one digit remains.
# Example Input: Number = 9876
# Example Output: Final Result = 3


def singledigitsum(num):
    while num >= 10:
        total = 0
        while num > 0:
            digit = num % 10
            total += digit
            num //= 10
        num = total
    return num
print(singledigitsum(9876))

# 8. Second Largest Digit
# Task: Find the second largest digit in a number.
# Example Input: Number = 58392
# Example Output: Largest = 9, Second largest = 8

def secondlargest(num):
    largest=0
    secondlargest = 0
    while num > 0:
        digit = num % 10
        if digit > largest:
            secondlargest = largest
            largest = digit
        elif digit>secondlargest and digit!=largest:
            secondlargest = digit
        num //= 10
    return largest,secondlargest
largest, secondlargest = secondlargest(58392)
print("Largest Digit:", largest)
print("Second Largest Digit:", secondlargest)

# 9. Replace Zero Digits
# Task: Replace all zero digits with 9.
# Example Input: Number = 102030
# Example Output: Result = 192939

def replacedigit(num):
    result = ""
    while num > 0:
        digit = num % 10
        if digit == 0:
            digit = 9
        result=str(digit)+result
        num //= 10
    return int(result)
print(replacedigit(102030))

# 10. Digit Position Finder
# Task: Find position of a digit in a number from right side.
# Example Input: Number = 58392, Digit = 3
# Example Output: Position = 3

def positionfinder(num,target):
    count = 0
    while num>0:
        digit = num % 10
        count+=1
        if digit == target:
            return count
        num //= 10
print(f'The Position of digit is:{positionfinder(58392,3)}')

