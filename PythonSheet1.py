# 1. Swap Two Numbers Without Third Variable
# Definition: Exchange values of two variables without using an extra variable.
# Task: Swap using arithmetic operators and bitwise XOR.
# Example Input: A=15, B=25
# Example Output: A=25, B=15
# using: Arithmetic Operators

def swapnum(a, b):
    print("Before Swapping")
    print("A =", a)
    print("B =", b)

    a = a + b
    b = a - b
    a = a - b

    print("\nAfter Swapping")
    print("A =", a)
    print("B =", b)
a = int(input("Enter A: "))
b = int(input("Enter B: "))
swapnum(a, b)


#Using bitwiseXOR
def swapnum(a, b):
    print("Before Swapping")
    print("A =", a)
    print("B =", b)

    a = a ^ b
    b = a ^ b
    a = a ^ b

    print("\nAfter Swapping")
    print("A =", a)
    print("B =", b)

a = int(input("Enter A: "))
b = int(input("Enter B: "))

swapnum(a, b)


# 2. Convert Seconds Into Hours, Minutes and Seconds
# Definition: Convert total seconds into time units.
# Task: Find hours, minutes and remaining seconds.
# Example Input: Total seconds=7384
# Example Output: Hours=2, Minutes=3, Seconds=4

def timeconvertor(totalsec):
    hours = totalsec // 3600
    remainingseconds = totalsec % 3600
    
    minutes = remainingseconds // 60
    seconds = remainingseconds % 60
    
    return f'Hours={hours},minutes={minutes},seconds={seconds}'
    
totalsec=int(input("Total Seconds: "))
print(timeconvertor(totalsec))


# 3. Temperature Conversion System
# Definition: Convert temperature values between Celsius and Fahrenheit.
# Task: Convert Celsius to Fahrenheit and Fahrenheit to Celsius.
# Example Input: Celsius=30
# Example Output: Fahrenheit=86

def tempconversion(celsius, farenheit):
    f = (9/5 * celsius) + 32
    c = (5/9) * (farenheit - 32)

    print("Celsius to Fahrenheit =", f)
    print("Fahrenheit to Celsius =", c)

tempconversion(30, 86)


# 4. Calculate Compound Amount
# Definition: Compound interest calculates interest on both the original amount and previously earned
# interest.
# Task: Calculate final amount using the compound interest formula.
# Formula:
# Amount = P × (1 + R/100)^T
# Where:
# P = Principal amount
# R = Rate of interest
# T = Time period
# Example Input:
# Principal = 10000
# Rate = 10
# Time = 2 years
# Example Output:
# Final Amount = 12100

def intrestCalculator(principle,rate,time):
    amount = principle * ( 1 + rate / 100) ** time
    return f'The Final Amount:{amount:.2f}'
print(intrestCalculator(10000,10,2))


# 5. Split Bill Among Friends
# Definition: Divide a total bill equally among people.
# Task: Find each person's share and remaining amount.
# Example Input: Bill=2455, Friends=5
# Example Output: Each pays=491, Remaining=0

def splitbill(bill,members):
    total = bill / members
    remaining = bill - total*members
    return f'Each Pays:{total},Remaining:{remaining}'
bill = int(input("Bill: "))
members = int(input("Friends: "))
print(splitbill(bill,members))


# 6. Convert Distance Units
# Definition: Convert kilometers into smaller units.
# Task: Convert km into meters, centimeters and millimeters.
# Example Input: Distance=5 km
# Example Output: Meters=5000, Centimeters=500000, Millimeters=5000000

def distanceConverter(distance):
    meters = distance * 1000
    centimeters = distance * 100000
    millimeters = distance * 1000000
    return f'meters = {meters},centimeters = {centimeters},millimeters = {millimeters}'
distance = int(input("Distance in Km: "))
print(distanceConverter(distance))


# 7. Digital Storage Conversion
# Definition: Convert storage units from GB to smaller units.
# Task: Convert GB into MB, KB and Bytes.
# Example Input: Storage=2 GB
# Example Output: MB=2048, KB=2097152, Bytes=2147483648

def storageConversion(gb):
    mb = gb * 1024
    kb = gb * 1048576 #1024 * 1024 = 1048576
    bytes = gb * 1073741824 # 1024 * 1024 * 1024 = 1073741824
    return f'MB={mb},KB={kb},Bytes={bytes}'
gb = int(input("Storage in GB= "))
print(storageConversion(gb))


# 8. Minimum Currency Notes
# Definition: Find the number of currency notes required for an amount.
# Task: Use 500, 200, 100 and 50 denomination notes.
# Example Input: Amount=1850
# Example Output: 500 notes=3, 200 notes=1, 100 notes=1, 50 notes=1

def currencynotes(amount):
    note500 = amount // 500
    amount = amount % 500

    note200 = amount // 200
    amount = amount % 200

    note100 = amount // 100
    amount = amount % 100

    note50 = amount // 50
    amount = amount % 50

    return f'500 Notes = {note500},200 Notes{note200},100 Notes = {note100},50 Notes = {note50}'
amount = int(input("Amount: "))
print(currencynotes(amount))


# 9. Salary Calculation System
# Definition: Calculate final salary after adding bonus and deducting tax.
# Task: Calculate the final salary.
# Example Input: Salary=40000, Bonus=5000, Tax=10%
# Example Output: Final Salary=40500

def salaryCal(salary):
    total = salary + bonus
    tax = total * 10 / 100
    Finalsal = total - tax
    
    return f'Final Salary = {Finalsal}'

salary = int(input("Salary: "))
bonus = int(input("Bonus: "))
tax = int(input("Tax: "))
print(salaryCal(salary))



# 10. Travel Time Calculator
# Definition: Calculate travel duration using distance and speed.
# Task: Find time for two journeys and total time.
# Formula: Time = Distance / Speed
# Example Input: Distance1=120, Speed1=60, Distance2=100, Speed2=50
# Example Output: Journey1=2 hours, Journey2=2 hours, Total=4 hours

def timecalculator(distance1,speed1,distance2,speed2):
    journey1 = distance1 / speed1
    journey2 = distance2 / speed2
    total = journey1 + journey2

    return f'Journey1={journey1} hours,journey2={journey2} hours,Total={total} hours'

distance1 = int(input("Distance1: "))
speed1 = int(input("Speed1: "))
distance2 = int(input("Distance2: "))
speed2 = int(input("Speed2: "))

print(timecalculator(distance1,speed1,distance2,speed2))









