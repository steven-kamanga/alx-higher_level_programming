#!/usr/bin/python3

for i in range(ord('z'), ord('a') - 1, -1):
    if i % 2 == 0:
        print(chr(i).lower(), end='')
    else:
        print(chr(i).upper(), end='')
