#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter16/shell.py
# A simple shell, so you can try running commands in the absence of
# any special characters (except for whitespace, used for splitting).

import subprocess

while True:
    args = input('] ').split()
    if not args:
        pass
    elif args == ['exit']:
        break
    elif args[0] == 'show':
        print("Arguments:", args[1:])
    else:
        subprocess.call(args)
