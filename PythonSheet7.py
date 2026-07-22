# 1. Count Passing Students
# Task: Read marks of N students. Count how many scored 35 or more.
# Example Input:
# 5
# 45
# 20
# 67
# 35
# 18
# Example Output:
# 3

n = int(input("Enter N students: "))
count = 0
for i in range(1,n+1):
    num = int(input("Enter Marks: "))
    if num >= 35:
        count+=1
print(count)

# 2. Shop Profit Days
# Task: Read profit for N days. Count days with profit greater than Rs.1000.
# Example Input:
# 5
# 800
# 1200
# 1500
# 950
# 2000
# Example Output:
# 3

n = int(input("Enter N value: "))
count = 0
for i in range(1,n+1):
    profit = int(input("Enter Profits: "))
    if profit > 1000:
        count+=1
print(count)

# 3. Largest Multiple of 5
# Task: Read N numbers. Print the largest divisible by 5, else 'No Multiple of 5'.
# Example Input:
# 5
# 12
# 25
# 18
# 40
# 7
# Example Output:
# 40

n = int(input("Enter N value: "))
largest = 0
for i in range(1,n+1):
    num = int(input("Enter numbers: "))
    if num%5==0:
        if num>largest:
            largest = num
if largest==-1:
    print('no multiples of 5')
else:
    print(largest)

# 4. Average of Even Numbers
# Task: Read N numbers. Print average of even numbers, else 'No Even Numbers'.
# Example Input:
# 5
# 2
# 5
# 8
# 7
# 10
# Example Output:
# Average = 6.67

n = int(input("Enter N value: "))
sum = 0
count = 0
for i in range(1,n+1):
    num = int(input("Enter numbers: "))
    if num%2==0:
        count+=1
        sum+=num
    average = sum / count
if count>0:
    print(average)
else:
    print("No even numbers")


# 5. Student Improvement
# Task: Read marks in N tests. Count how many times marks increased.
# Example Input:
# 5
# 50
# 55
# 52
# 60
# 70
# Example Output:
# 3

n=int(input('enter N tests:'))
count=0
prevmarks=int(input("Enter the marks: "))
for i in range(2,n+1):
    marks=int(input("Enter the marks: "))
    if marks>prevmarks:
        count+=1
        prevmarks=marks
print(count)

# 6. Divisors Count
# Task: Read a number and count its divisors.
# Example Input:
# 12
# Example Output:
# 6

n = int(input("Enter number: "))
i = 1
count = 0
while i <= n:
    if n%i==0:
        count+=1
    i+=1
print(count)


# 7. Smallest Odd Number
# Task: Read N numbers. Print smallest odd number or 'No Odd Number'.
# Example Input:
# 5
# 8
# 13
# 6
# 5
# 10
# Example Output:
# 5

n = int(input("Enter numbers: "))
count = 0
smallest = 0
for i in range(1,n+1):
    num = int(input("Enter numbers: "))
    if num%2==1:
        if smallest == 0 or num < smallest:
            smallest = num
        count+=1
if smallest > 0:
    print(smallest)
else:
    print("No odd numbers")

# 8. Count Numbers Ending with 7
# Task: Read N numbers. Count numbers ending with digit 7.
# Example Input:
# 5
# 27
# 15
# 97
# 120
# 47
# Example Output:
# 3

n = int(input("Enter N value: "))
count = 0
for i in range(1,n+1):
    num = int(input("Enter Numbers: "))
    digit = num % 10
    if digit == 7:
        count+=1
print(count)

# 9. Multiplication Table
# Task: Read a number and print table from 1 to 15.
# Example Input:
# 7
# Example Output:
# 7 x 1 = 7 ... 7 x 15 = 105

n = int(input("Enter number: "))
for i in range(1,16):
    print(f'{n} x {i} = {n*i}')


# 10. Sum Until Negative Number
# Task: Read numbers until a negative number is entered. Print sum of positive numbers.
# Example Input:
# 5
# 10
# 8
# 2
# -1
# Example Output:
# 25
sum=0
while True:
    num=int(input("Enter a number: "))
    if num < 0:
        break
    sum+=num
print(sum)





