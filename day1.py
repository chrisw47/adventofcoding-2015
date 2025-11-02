instructions = open('day1.txt', 'r').read()

# print(len(instructions))

counter = 0
position = 0

for par in instructions:
    if counter == -1:
        print(f'Position: {position}')
        break
    else:
        if par == '(':
            counter += 1
            position += 1
        elif par == ')':
            counter -= 1
            position += 1
        else:
            print('Not a valid instruction for Santa.')

# print(f'The floor Santa should end up on is: {counter}.')