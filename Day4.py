# 1. Count Total Keys
# Task:
# Write a function that returns the total number of keys in a dictionary.
# Example Input:
# {"a":10,"b":20,"c":30}
# Example Output:
# 3
# def totalnumofkeys(keys):
#     count = 0
#     for key in keys:
#         count+=1
#     return count
# dict1 = {"a":10,"b":20,"c":30}
# print(f'Total Number of keys:{totalnumofkeys(dict1)}')

# 2. Find the Key with the Largest Value
# Task:
# Return the key whose value is the largest.
# Example Input:
# {"Math":78,"Science":92,"English":85}
# Example Output:
# Science

# def largestvalue(keys):
#     largest = ""
#     largestvalue = 0
#     for key in keys:
#         if keys[key] > largestvalue:
#             largestvalue = keys[key]
#             largest = key
#     return largest
# dict1={"Math":78,"Science":92,"English":85}
# print(f'The Largest Key is:{largestvalue(dict1)}')


# 3. Find the Key with the Smallest Value
# Task:
# Return the key whose value is the smallest.
# Example Input:
# {"Math":78,"Science":92,"English":65}
# Example Output:
# # English

# def smallestvalue(keys):
#     smallestkey = ""
#     first = True
#     for key in keys:
#         if first:
#             smallest_value = keys[key]
#             smallestkey = key
#             first = False
#         elif keys[key] < smallest_value:
#             smallest_value = keys[key]
#             smallestkey = key
#     return smallestkey
# dict1 = {"Math": 78, "Science": 92, "English": 65}
# print("The Smallest Key is:", smallestvalue(dict1))


# 4. Sum of All Values
# Task:
# Return the sum of all values in the dictionary.
# Example Input:
# {"Pen":20,"Book":150,"Bag":500}
# Example Output:
# 670

# def sumofallvalues(nums):
#     count = 0
#     for num in nums:
#         count += nums[num]
#     return count
# dict1 = {"Pen":20,"Book":150,"Bag":500}
# print(f'The sum of values are:{sumofallvalues(dict1)}')


# 5. Count Even Values
# Task:
# Return how many values in the dictionary are even.
# Example Input:
# {"a":10,"b":7,"c":16,"d":5}
# Example Output:
# 2

# def countevenvalues(nums):
#     count = 0
#     for num in nums:
#         if nums[num]%2 == 0:
#             count += 1
#     return count
# dict1={"a":10,"b":7,"c":16,"d":5}
# print(f'The count of even values:{countevenvalues(dict1)}')

# 6. Count Values Greater Than a Target
# Task:
# Given a target number, count how many dictionary values are greater than it.

# Example Input:
# Dictionary={"A":45,"B":80,"C":65,"D":90}
# Target=70

# Example Output:
# 2

# def valuegreater(nums,target):
#     count = 0
#     for num in nums:
#         if nums[num] > target:
#             count += 1
#     return count
# dict1 = {"A":45,"B":80,"C":65,"D":90}
# print(f'Target:{valuegreater(dict1,70)}')


# 7. Create a Dictionary of Squares
# Task:
# Given a list of numbers, create a dictionary where the number
# is the key and its square is the value.
# Example Input:
# [2,3,4,5]
# Example Output:
# {2:4,3:9,4:16,5:25}

# def dictofsquares(nums):
#     squares = {}
#     for num in nums:
#         squares[num] = num * num
#     return squares
# list1 = [2,3,4,5]
# print(dictofsquares(list1))

# 8. Count Positive Values
# Task:
# Return the number of positive values in the dictionary.

# Example Input:
# {"a":-5,"b":10,"c":0,"d":8}

# Example Output:
# 2

# def positivevalue(nums):
#     count = 0
#     for num in nums:
#         if nums[num] > 0:
#             count+=1
#     return count
# dict1 = {"a":-5,"b":10,"c":0,"d":8,"e":3}
# print(f'The Count of positive NUmbers:{positivevalue(dict1)}')



# 9. Find the Average of All Values
# Task:
# Return the average of all values in the dictionary.

# Example Input:
# {"A":10,"B":20,"C":30}

# Example Output:
# 20.0

# def average(nums):
#     total = 0
#     count = 0
#     for num in nums:
#         total+=nums[num]
#         count+=1
#         average = total / count
#     return average
# dict1 = {"A":10,"B":20,"C":30}
# print(f'The Average is:{average(dict1)}')


# 10. Reverse Key and Value
# Task:
# Create a new dictionary where the values become keys and the keys 
# become values.

# Example Input:
# {"A":1,"B":2,"C":3}

# Example Output:
# {1:"A",2:"B",3:"C"}

def reverse(dict):
    reversedict = {}
    for key in dict:
        reversedict[dict[key]] = key
    return reversedict
dict1 = {"A": 1, "B": 2, "C": 3}
print(reverse(dict1))



