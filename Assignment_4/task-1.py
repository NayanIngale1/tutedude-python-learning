

try:
  
  sample_file = open('sample.txt')

  print(f'Line 1: {sample_file.readline()}')
  print(f'Line 2: {sample_file.readline()}')
  
except FileNotFoundError:
  print('Error: The file \'sample.txt\' was not found.')