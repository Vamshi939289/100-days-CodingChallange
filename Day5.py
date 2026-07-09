# 1. Seating Arrangement Checker
# Task: Find occupied seats, empty seats, and row with maximum occupancy.
# Input: seats=[[1,0,1,1],[0,1,1,0],[1,1,1,1]]
# Output: Occupied Seats=9, Empty Seats=3, Row with Maximum Occupancy=Row 3

def seatingarrangement(seats):
    occupied = 0
    empty = 0
    max_occupied = 0
    max_row = 0
    for i in range(len(seats)):
        count = 0
        for j in range(len(seats[i])):
            if seats[i][j] == 1:
                occupied += 1
                count += 1
            else:
                empty += 1
        if count > max_occupied:
            max_occupied = count
            max_row = i + 1
    print("Occupied Seats =", occupied)
    print("Empty Seats =", empty)
    print("Row with Maximum Occupancy = Row", max_row)
seats = [[1, 0, 1, 1],[0, 1, 1, 0],[1, 1, 1, 1]]
seatingarrangement(seats)


#2. Product Price Comparison
# Task: Find cheapest price for each product and store.
# Input: prices=[[100,120,90],[250,200,300],[50,70,60]]
# Output: Product 1=90(Store 3), Product 2=200(Store 2), Product 3=50(Store 1)

def productComparison(prices):
    for i in range(len(prices)):
        cheapestprice = prices[i][0]
        store = 1
        for j in range(len(prices[i])):
            if prices[i][j] < cheapestprice:
                cheapestprice = prices[i][j]
                store = j + 1

        print("product", i + 1,"=",cheapestprice,"(Store", store, ")")
prices=[[100,120,90],[250,200,300],[50,70,60]]
productComparison(prices)


# 3. Word Search in a Grid
# Task: Count occurrences of a given character.
# Input: grid=[['p','y','t'],['h','o','n'],['p','y','t']], character='p'
# Output: p found 2 times

def countoccurance(words,target):
    count = 0
    for i in range(len(words)):
        for j in range(len(words[i])):
            if words[i][j] == target:
                count+= 1
    print(target,"found",count,"times")
words=[['p','y','t'],['h','o','n'],['p','y','t']]
countoccurance(words,'p')

# 5. Password Strength Analyzer
# Task: Count uppercase, lowercase and digits and classify password.
# Input: passwords=['Abc123','hello','P@55']
# Output: Abc123 Strong, hello Weak, P@55 Strong

def password_strength(passwords):
    for i in range(len(passwords)):
        upper = 0
        lower = 0
        digit = 0
        for j in range(len(passwords[i])):
            ch = passwords[i][j]
            if 'A' <= ch <= 'Z':
                upper += 1
            elif 'a' <= ch <= 'z':
                lower += 1
            elif '0' <= ch <= '9':
                digit += 1
        if upper > 0 and lower > 0 and digit > 0:
            print(passwords[i], "Strong")
        else:
            print(passwords[i], "Weak")
passwords = ['Abc123', 'hello', 'P@55']
password_strength(passwords)


# 6. Image Pixel Brightness Analyzer Task: Count dark,
# medium and bright pixels. Input: 
#     image=[[20,80,200],[40,150,220]]
#     Output: Dark=2, Medium=2, Bright=2

def brightness(image):
    dark = 0
    medium = 0
    bright = 0

    for i in range(len(image)):
        for j in range(len(image[i])):

            if image[i][j] < 50:
                dark += 1
            elif image[i][j] <= 150:
                medium += 1
            else:
                bright += 1

    print("Dark =", dark)
    print("Medium =", medium)
    print("Bright =", bright)
image = [[20, 80, 200],[40, 150, 220]]
brightness(image)






# 9. Monthly Expense Category Tracker Task: Find highest expense and categories above limit. 
# Input: expenses=[[500,200,800],[300,700,100],[900,400,600]], 
# limit=500 Output: Person 1 Highest=800, Categories Above Limit=4



def expensetracker(expenses,limit):
    above = 0
    for i in range(len(expenses)):
        highest = expenses[i][0]
        for j in range(len(expenses[i])):
            if expenses[i][j] > highest:
                highest = expenses[i][j]
            if expenses[i][j] > limit:
                above += 1
        print("Person", i + 1, "Highest =", highest)
    print("Categories Above Limit =", above)
expenses = [[500, 200, 800],[300, 700, 100],[900, 400, 600]]
expensetracker(expenses, 500)

# 10. Chess Board Analyzer Task: Count white pieces, black pieces 
# and empty positions. Input: board=[['W','B','-'],['B','W','-'],['-','W','B']] 
# Output: White=3, Black=3, Empty=3

def chessboard(board):

    white = 0
    black = 0
    empty = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'W':
                white += 1
            elif board[i][j] == 'B':
                black += 1
            else:
                empty += 1
    print("White =", white)
    print("Black =", black)
    print("Empty =", empty)

board=[['W','B','-'],['B','W','-'],['-','W','B']]
chessboard(board)