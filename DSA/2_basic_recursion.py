# Basic Recursion


# Syntax:

'''
def function( parameters ):

    base condition
    if

    return recursive equation


'''

# que: factorial of n

# normal iterative code:

'''
n = int(input("Enter a num: "))
ans = 1
for i in range(1,n+1):
  ans *= i

print(f'factorial of {n} is {ans}')

'''

# recursion code:

'''
def factorial(n: int):
    if n == 1 or n == 0:
        return 1

    return n * factorial(n-1)


n = int(input("Enter a num: "))
print(f'factorial of {n} is {factorial(n)}')

'''

# que: nth fibonaci number
# A Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8....
# The first two terms are 0 and 1. All other terms are obtained by adding
# the preceding two terms. This means to say the nth term is the
# sum of(n-1)th and (n-2)th term.


# normal code:
'''

def fibbo(n):
    arr = []
    for i in range(0, n):
        if i == 0 or i == 1:
            arr.append(i)
            continue

        arr.append(arr[len(arr)-1]+arr[len(arr)-2])

    print(arr)


fibbo(n)
n = int(input('Enter number of terms: '))

'''

# recursive code:

'''
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


print(fibonacci_recursive(10))

n = int(input("Enter number of terms: "))
for i in range(n):
    print(fibonacci_recursive(i), end=' ')

'''
