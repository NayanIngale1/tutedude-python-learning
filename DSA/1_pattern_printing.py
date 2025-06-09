#  Basic patterns

# que: print pattern like below
# where n = 3 and m = 4
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4

'''
n = int(input('Rows: '))
m = int(input('Columns: '))


for i in range(1, n+1):
  for j in range(1, m+1):
    print(j, end = ' ')
    
  print("")
'''

# que: print pattern like below
# where n = 4
# 1
# 1 2
# 1 2 3
# 1 2 3 4


'''
n = int(input("Rows: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")

    print("")

'''

# que: print pattern like below
# where n = 4
#       *
#     * *
#   * * *
# * * * *

'''
n = int(input('Rows: '))

for i in range(1, n+1):
    line = ''
    for j in range(1, n+1):
        if j <= n - i:
            line += '  '
        else:
            line += '* '
    print(line)

'''
