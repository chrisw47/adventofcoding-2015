directions = open('day3.txt', 'r').read()

def move_santa(instr: str, address: list):

    if instr == '^':
        new_add = [address[0], address[1] + 1]
    elif instr == 'v':
        new_add = [address[0], address[1] - 1]
    elif instr == '>':
        new_add = [address[0] + 1, address[1]]
    elif instr == '<':
        new_add = [address[0] - 1, address[1]]
    
    return new_add

# Part 1

addresses = [[0, 0]]

for inst in directions:
    old_address = addresses[-1]
    addresses.append(move_santa(inst, old_address))

unique_addresses = []

for address in addresses:
    if address not in unique_addresses:
        unique_addresses.append(address)

print(f'Santa visits {len(unique_addresses)} houses in total for part 1.')

# Part 2

addresses = [[0, 0]]

santa_dirs = ''
robo_dirs = ''

for i, dir in enumerate(directions):
    if i % 2 == 0:
        santa_dirs += dir
    elif i % 2 == 1:
        robo_dirs += dir

s_addresses, r_addresses = addresses, addresses

for inst in santa_dirs:
    old_address = addresses[-1]
    addresses.append(move_santa(inst, old_address))

addresses.append([0, 0])

for inst in robo_dirs:
    old_address = addresses[-1]
    addresses.append(move_santa(inst, old_address))

unique_addresses = []

for address in addresses:
    if address not in unique_addresses:
        unique_addresses.append(address)

print(f'Santa visits {len(unique_addresses)} houses in total for part 2.')