# Basic list questions


#  take input for list

#  method 1:

'''
myList = []

n = int(input('lenght of list: '))
for i in range(n):
    curEle = int(input())
    myList.append(curEle)

print(myList)
'''

# method 2:

'''
myList = input().split(" ")

for i in range(len(myList)):
    myList[i] = int(myList[i])

print(myList)

'''


def takeListInput():
    n = int(input('length of list: '))
    myList = input('list elements: ').strip().split(" ")

    for i in range(n):
        myList[i] = int(myList[i])

    return myList[:n]


# que: find the sum of all the elements in the list

'''
myList = takeListInput()
print(myList)
sumOfList = 0
for i in range(len(myList)):
    sumOfList += myList[i]

print(f'total sum of list: {sumOfList}')

'''


# que: find min and max from list


'''
myList = takeListInput()

# we have min and max inbuilt functions which finds the min and max elements from list
# min(myList)
# max(myList)

minEle = myList[0]
maxEle = myList[0]

for val in myList:
  if val < minEle:
    minEle = val
  if val > maxEle:
    maxEle = val

print(f'{minEle} is min and {maxEle} is max in the given list.')

'''


# que: find mean, median and mode of list
# mean = sum of list / length of list
# median = middle value when data is sorted.
# mode = most frequently occurring value

'''
myList = takeListInput()
n = len(myList)

sumOfList = sum(myList)

mean = sumOfList / n
print(f'mean is {mean}')


sortedMyList = myList.copy()
sortedMyList.sort()

if n % 2 == 0:
    ele1 = sortedMyList[n//2 - 1]
    ele2 = sortedMyList[n//2]
    median = (ele1 + ele2) / 2
else:
    median = sortedMyList[n//2]

print(f'median is {median}')


# mode can be find by various methods
# method 1:

# maxCount = 0
# maxEle = myList[0]

# for currEle in myList:
#     currCount = 0
#     for eachEle in myList:
#         if currEle == eachEle:
#             currCount += 1

#     if currCount > maxCount:
#         maxCount = currCount
#         maxEle = currEle
# print(f'mode is {maxEle} with max count {maxCount}')


# method 2:

maxCount = 0
maxEle = sortedMyList[0]
currCount = 1

for i in range(n-1):
    if sortedMyList[i] == sortedMyList[i+1]:
        currCount += 1
    else:
        if currCount > maxCount:
            maxCount = currCount
            maxEle = sortedMyList[i]
        currCount = 1

if currCount > maxCount:
    maxCount = currCount
    maxEle = sortedMyList[-1]


print(f'mode is {maxEle} with max count {maxCount}')

'''


# Slicing and list comprehension

# slicing syntax
# myList[start : end : step]


# myList = [1, 2, 3, 4, 5, 6]

# print(myList[::-1])

# comprehension syntax

# myList = [ele for ele in seq]

# myList = [ele*2 for ele in range(5)]

# print(myList)


# 2D list: list that itself contains list
# ex:
# grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(grid)
# print(grid[0])
# print(grid[0][1])


def take2DInput():
    grid = []
    n = int(input("Enter rows of metrix: "))
    m = int(input("Enter columns of metrix: "))

    for i in range(n):
        grid.append([int(ele) for ele in input().strip().split()[:m]])

    return grid


# print(take2DInput())


# que: find the trace of a square n x n matrix
# The trace is the sum of all the elements on the main diagonal of a square matrix

'''
matrix = take2DInput()
n = len(matrix)

trace = []
for i in range(n):
    trace.append(matrix[i][i])

print(sum(trace))

'''

# que: Transpose of a Matrix in Python
# The transpose of a matrix is obtained by
# flipping rows and columns — that is, matrix[i][j] becomes matrix[j][i].

# ex:
'''
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]  transpose of this matrix is ->
[
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]
'''

matrix = take2DInput()
n = len(matrix)


for i in range(n):
    for j in range(n):
        if j > i:
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


print(matrix, '<--transpose matrix')
