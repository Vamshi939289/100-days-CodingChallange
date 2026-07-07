# 1. Count Even Numbers
# Write a function that returns the number of even numbers in a list.
# Example
# Input: [2, 5, 8, 11, 14]
# Output: 3

# list1 = [2, 5, 8, 11, 14]
# def evenNum(list1):
#     even_count = 0
#     for num in list1:
#         if num%2==0:
#             even_count+=1
#     return even_count
# print(f'The Even number count in the list:{evenNum(list1)}')


# 2. Find the Largest Element
# Return the largest element in a list.
# Example
# Input: [12, 45, 7, 89, 23]
# Output: 89

# list1 = [12, 45, 7, 89, 23]
# def largest(list1):
#     largest = list1[0]      
#     for num in list1:
#         if num > largest:
#             largest = num
#     return largest
# print(f'The largest element in the list is: {largest(list1)}')





# 3. Find the Smallest Element
# Return the smallest element in a list.
# Example
# Input: [12, 45, 7, 89, 23]
# Output: 7

# list1 =  [12, 45, 7, 89, 23]
# def smallest(list1):
#     smallest=list1[0]
#     for num in list1:
#         if num < smallest:
#             smallest = num
#     return smallest
# print(f'The smallest number in list1 is:{smallest(list1)}')


# 4. Reverse a List
# Return the list in reverse order.
# Example
# # Input: [1, 2, 3, 4, 5]
# # Output: [5, 4, 3, 2, 1]

# list1 = [1, 2, 3, 4, 5]
# def rev(list1):
#     reverse = []
#     for num in list1:

#         reverse.insert(0, num)
#     return reverse
# print(rev(list1))



# 5. Sum of All Elements
# Return the sum of all numbers in the list.
# Example
# Input: [4, 8, 10]
# Output: 22


# list1 = [4, 8, 10]
# def addEle(list1):
#     count = 0
#     for num in list1:
#         count+=num
#     return count
# print(f'Sum of Elements:{addEle(list1)}')

# 6. Count Occurrences
# Count how many times a target appears.
# Example
# Input: List=[1,2,3,2,4,2], Target=2
# Output: 3

# list1 = [1, 2, 3, 2, 4, 2]

# def countOccurrence(list1, target):
#     count = 0
#     for num in list1:
#         if num == target:
#             count += 1
#     return count
# print(countOccurrence(list1, 2))

# 7. Remove Duplicates
# Remove duplicates while preserving order.
# Example
# Input: [1,2,2,3,1,4]
# Output: [1,2,3,4]

# list1 = [1, 2, 2, 3, 1, 4]

# def remDupli(list1):
#     result = []
#     for num in list1:
#         if num not in result:
#             result.append(num)
#     return result
# print(remDupli(list1))


# 8. Find the Average
# Return the average of all numbers.
# Example
# Input: [10,20,30,40]
# Output: 25.0

# list1 = [10, 20, 30, 40]
# def average(list1):
#     total = 0
#     count = 0
#     for num in list1:
#         total += num
#         count += 1
#     return total / count
# print(average(list1))


# 9. Create a List of Squares
# Return a new list containing the square of every element.
# Example
# Input: [2,3,4,5]
# Output: [4,9,16,25]


# list1 = [2, 3, 4, 5]
# def squareList(list1):
#     result = []
#     for num in list1:
#         result.append(num * num)
#     return result
# print(squareList(list1))


# 10. Count Positive Numbers
# Return the number of positive numbers.
# Example
# Input: [-2,5,0,7,-1,9]
# Output: 3

list1 = [-2,5,0,7,-1,9]
def countpositivenum(list1):
    count = 0
    for num in list1:
        if num > 0:
            count+=1
    return count
print(f'Positive Numbers:{countpositivenum(list1)}')