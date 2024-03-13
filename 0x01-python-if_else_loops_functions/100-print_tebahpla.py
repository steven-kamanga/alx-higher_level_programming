#!/usr/bin/python3
print(''.join('{}{}'.format(chr(i).lower(), chr(i - 1).upper()) for i in range(ord('z'), ord('a'), -2)))
