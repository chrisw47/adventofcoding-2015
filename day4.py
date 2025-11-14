import hashlib

k = 'iwrupvqb'  # key
dec = 1  # number to add to key
# leading zeros in final hash. part 1 requires 5 leading zeros, part 2 requires 6.
LEAD_ZERO = 6

r = hashlib.md5(k.encode())  # result after MD5 hash

while r.hexdigest()[:LEAD_ZERO] != '0' * LEAD_ZERO:
    k_new = k + str(dec)
    r = hashlib.md5(k_new.encode())
    dec += 1

print(f'Final string:\t{k_new}')
print(f'Resultant hash:\t{r.hexdigest()}')
