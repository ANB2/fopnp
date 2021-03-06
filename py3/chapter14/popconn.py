#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter14/popconn.py

import getpass, poplib, sys

if len(sys.argv) != 3:
    print('usage: %s hostname user' % sys.argv[0])
    exit(2)

hostname, user = sys.argv[1:]
passwd = getpass.getpass()

p = poplib.POP3_SSL(hostname)  # or "POP3" if SSL is not supported
try:
    p.user(user)
    p.pass_(passwd)
except poplib.error_proto as e:
    print("Login failed:", e)
else:
    status = p.stat()
    print("You have %d messages totaling %d bytes" % status)
finally:
    p.quit()
