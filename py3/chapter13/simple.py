#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter13/simple.py

import sys, smtplib

if len(sys.argv) < 4:
    print("usage: %s server fromaddr toaddr [toaddr...]" % sys.argv[0])
    sys.exit(2)

server, fromaddr, toaddrs = sys.argv[1], sys.argv[2], sys.argv[3:]

message = """To: %s
From: %s
Subject: Test Message from simple.py

Hello,

This is a test message sent to you from the simple.py program
in Foundations of Python Network Programming.
""" % (', '.join(toaddrs), fromaddr)

s = smtplib.SMTP(server)
s.sendmail(fromaddr, toaddrs, message)
s.quit()

print("Message successfully sent to %d recipient(s)" % len(toaddrs))
