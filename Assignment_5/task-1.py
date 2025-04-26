data = {
    'Alice': 85,
    'John': 90,
    'Peter': 56,
    'Bobby': 78
}


name = input("Enter the student's name: ").capitalize()
try:
    marks = data[name]
    print(f'{name}\'s marks: {marks}')
except Exception:
    print('Student not found!')
