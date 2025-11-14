import re

strings = open('day5.txt', 'r').read().splitlines()

# Part 1

GOOD_STRINGS = 0

for line in strings:
    if (len(re.findall(r'[aeiou]', line)) >= 3) and (len(re.findall(r'(\w)\1', line)) >= 1) and (len(re.findall(r'(ab|cd|pq|xy)', line)) == 0):
        GOOD_STRINGS += 1

print(f'PART 1: There are {GOOD_STRINGS} nice strings in the input.')

# Part 2

NICE_STRINGS = 0

for line in strings:
    pairs = re.findall(r'(?P<f>\w\w).*(?P=f)', line)
    ones = re.findall(r'(?P<s>\w).(?P=s)', line)
    if (len(pairs) >= 1) and (len(ones) >= 1):
        NICE_STRINGS += 1

print(f'PART 2: With the updated rules, there are {NICE_STRINGS} nice strings.')