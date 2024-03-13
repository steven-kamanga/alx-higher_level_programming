#!/usr/bin/python3
result = ''.join(
    '{}{}'.format(chr(i).lower(), chr(i - 1).upper())
    for i in range(ord('z'), ord('a'), -2)
)
print(result)
