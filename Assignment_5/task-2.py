original_list = []

for i in range(1,11):
  original_list.append(i)
  
first_five = original_list[:5]
reversed_first_five = first_five.copy()
reversed_first_five.reverse()

print(f'Original list: {original_list}')
print(f'Extracted first five elements: {first_five}')
print(f'Reversed extracted elements: {reversed_first_five}')

