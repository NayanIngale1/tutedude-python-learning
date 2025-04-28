# Regular Expressions (regex) in Python - Beginner Notes
#
# This file explains all the basic 're' module functions with simple examples.
# Useful for beginners to remember and practice.

'''
import re  # Always import 're' module first

# -------------------------------------------------------
# 1. re.match(pattern, string, flags=0)
# Checks if the beginning of the string matches the pattern.

pattern = 'apple'
result = re.match(pattern, 'apple pie')
if result:
    print('re.match: Match found')
else:
    print('re.match: No match found')

# -------------------------------------------------------
# 2. re.search(pattern, string, flags=0)
# Searches the string for the first occurrence of the pattern.

search_result = re.search('p', 'apple pie')
if search_result:
    print('re.search: Match found at position', search_result.start())
else:
    print('re.search: No match found')

# -------------------------------------------------------
# 3. re.findall(pattern, string, flags=0)
# Returns a list of all non-overlapping matches.

findall_result = re.findall('p', 'apple pie')
print('re.findall:', findall_result)  # Output: ['p', 'p', 'p']

# -------------------------------------------------------
# 4. re.finditer(pattern, string, flags=0)
# Returns an iterator yielding match objects for all matches.

print('re.finditer:')
for match in re.finditer('p', 'apple pie'):
    print('Found at:', match.start(), '-', match.end())

# -------------------------------------------------------
# 5. re.sub(pattern, repl, string, count=0, flags=0)
# Replaces occurrences of the pattern with a replacement string.

sub_result = re.sub('apple', 'orange', 'apple pie and apple juice')
print('re.sub:', sub_result)  # Output: orange pie and orange juice

# -------------------------------------------------------
# 6. re.split(pattern, string, maxsplit=0, flags=0)
# Splits the string wherever the pattern matches.

split_result = re.split('p', 'apple pie')
print('re.split:', split_result)  # Output: ['a', '', 'le ', 'ie']

# -------------------------------------------------------
# 7. re.compile(pattern, flags=0)
# Compiles a pattern into a regex object for reuse.

compiled_pattern = re.compile('a')
compiled_result = compiled_pattern.findall('apple banana')
print('re.compile + findall:', compiled_result)  # Output: ['a', 'a', 'a', 'a']

# -------------------------------------------------------
# 8. re.fullmatch(pattern, string, flags=0)
# Checks if the entire string matches the pattern.

fullmatch_result = re.fullmatch('apple', 'apple')
if fullmatch_result:
    print('re.fullmatch: Full match found')
else:
    print('re.fullmatch: Full match not found')

# -------------------------------------------------------
# Beginner Summary:
#
# match()    --> Match only at the beginning
# search()   --> Search anywhere
# findall()  --> Find all matches and return list
# finditer() --> Find all matches and return iterator (match object)
# sub()      --> Substitute text (replace)
# split()    --> Split string based on pattern
# compile()  --> Create reusable pattern object
# fullmatch()--> Full string match

# -------------------------------------------------------
# Note:
# - By default, regex matching is case-sensitive.
# - Use flags like re.IGNORECASE if you want case-insensitive matching.

# Example with flag:
ignore_case_result = re.match('apple', 'APPLE', flags=re.IGNORECASE)
if ignore_case_result:
    print('Case-insensitive match found')
else:
    print('Case-insensitive match not found')

# -------------------------------------------------------
'''

# CHARACTERS AND CHARACTER SEQUENCES

# ^ - Matches the begining of the line 
# $ - Matches the end of the line
# . - Matches any character
# \d - Matches any digit
# \D - Matches any non-digit
# \s - Matches whitespace
# \S - Matches any non-whitespace
# * - Repeats a character zero or more time
# + - Repeats a character one or more time 
# ( - Indicates where a string extraction is to start
# ) - Indicates where a string extraction is to end
# ? - Matches the expression 0 to 1 time
# [] - 
# [aeiou] - Matches a single character in the listed set 
# [^xyz] - Matches a single character 
# [a-z 0-9] - Set of character can include a range
# {}

import re

# -------------------------------------------------------
# ^  - Matches the beginning of the line/string

text = "Hello world"
result = re.match(r'Hello', text)
print('^ Example:', bool(result))  # True because 'Hello' is at the beginning

# -------------------------------------------------------
# $  - Matches the end of the line/string

text = "This is Python"
result = re.search(r'Python$', text)
print('$ Example:', bool(result))  # True because 'Python' is at the end

# -------------------------------------------------------
# .  - Matches any single character (except newline)

text = "cat"
result = re.search(r'c.t', text)
# True because '.' matches any one character between 'c' and 't'
print('. Example:', bool(result))

# -------------------------------------------------------
# \d - Matches any digit (0-9)

text = "Order number is 12345"
result = re.findall(r'\d', text)
print(r'\d Example:', result)  # ['1', '2', '3', '4', '5']

# -------------------------------------------------------
# \D - Matches any non-digit

text = "abc123"
result = re.findall(r'\D', text)
print(r'\D Example:', result)  # ['a', 'b', 'c']

# -------------------------------------------------------
# \s - Matches any whitespace character (space, tab, newline)

text = "Hello World"
result = re.findall(r'\s', text)
print(r'\s Example:', result)  # [' '] (space found)

# -------------------------------------------------------
# \S - Matches any non-whitespace character

text = "Hello World"
result = re.findall(r'\S', text)
# ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd']
print(r'\S Example:', result)

# -------------------------------------------------------
# *  - Repeats a character zero or more times

text = "goooooal"
result = re.search(r'go*al', text)
print('* Example:', bool(result))  # True, because 'o' repeated many times

# -------------------------------------------------------
# +  - Repeats a character one or more times

text = "goooal"
result = re.search(r'go+al', text)
print('+ Example:', bool(result))  # True, at least one 'o' is required

# -------------------------------------------------------
# ( ) - Indicates where a string extraction is to start and end (capturing groups)

text = "Name: John"
result = re.search(r'Name: (.+)', text)
if result:
    print('( ) Example:', result.group(1))  # Captured 'John'

# -------------------------------------------------------
# ?  - Matches the expression 0 or 1 time (optional)

text = "color"  # Also matches "colour"
result = re.search(r'colou?r', text)
print('? Example:', bool(result))  # True

# -------------------------------------------------------
# [] - Set of characters to match

text = "dog"
result = re.search(r'[dg]', text)
print('[] Example:', bool(result))  # True because 'd' or 'g' is present

# -------------------------------------------------------
# [aeiou] - Matches any vowel (single character from listed set)

text = "python"
result = re.findall(r'[aeiou]', text)
print('[aeiou] Example:', result)  # ['o']

# -------------------------------------------------------
# [^xyz] - Matches any character except x, y, or z

text = "apple"
result = re.findall(r'[^xyz]', text)
print('[^xyz] Example:', result)  # ['a', 'p', 'p', 'l', 'e']

# -------------------------------------------------------
# [a-z0-9] - Set can include a range (lowercase letters and digits)

text = "abc123"
result = re.findall(r'[a-z0-9]', text)
print('[a-z0-9] Example:', result)  # ['a', 'b', 'c', '1', '2', '3']

# -------------------------------------------------------
# {} - Specifies exactly how many times a character should repeat

text = "Hellooo"
result = re.search(r'o{3}', text)
print('{} Example:', bool(result))  # True because there are exactly 3 'o's

# -------------------------------------------------------
