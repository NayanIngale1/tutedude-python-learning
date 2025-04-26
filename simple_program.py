'''
print("Hello there!")
input("Enter your age: ")
print("Thank you")

#Celsius ----> Farenheit
c = input('Celsius: ')
c = float(c)
fe = (c * 9/5) + 32
print(f'{c} Celsius is {fe} Ferenheit')

#Ferenheit ----> Celsius 
fe = input('Ferenheit: ')
fe = float(fe)
c = (fe - 32) * 5/9
c = round(c, 2)
print(f'{fe} Ferenheit is {c} Celsius')

# if (statement):
    #statement
#statement

a = 4
if a < 5:
  print('a is greater than 5')

print('Thank you')




# if (statement):
    #statement
#else:
    #statement
#statement

marks = int(input("Enter your marks: "))

if marks >= 40:
  print("PASSED")
else:
  print("FAILED")
  
print('Thank you!')


# if (test_expression):
#   statement
# elif (test_expression):
#   statement
# ....
# else:
#   statement

# statement


operand_1 = int(input('Enter operand 1: '))
operand_2 = int(input('Enter operand 2: '))
operator = input('Enter the operator (+,-,*,/): ')

if operator == '+':
    print(operand_1+operand_2)
elif operator == '-':
    print(operand_1-operand_2)
elif operator == '*':
    print(operand_1*operand_2)
elif operator == '/':
    print(operand_1/operand_2)
else:
    print("None")

print('Thank you!')


# range(start_value, end_value, step)

n = list(range(0, 12, 2))
print(n)



li = ['mike', 19.3, 1997]

for i in li:
    print(i, f'<--- item in list')


for i n range(1,11):
  print(i)

# while (test_expression):
#   statement
#   increment/decrement

counter = 1
while (counter <= 5):
    print('a')
    counter += 1


counter = 5
while counter >= 1:
    print('apple')
    counter -= 1
'''


dic = {
    'a': 'apple',
    'b': 'boll',
    'c': 'cat',
    'd': 'dog',
    'e': 'elephant'
}

print(dic.get('g','g is not Found')) 