#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter15/open_imaplib.py
# Opening an IMAP connection with the pitiful Python Standard Library

import getpass, imaplib, sys

def main():
    try:
        hostname, username = sys.argv[1:]
    except ValueError:
        print('usage: %s hostname username' % sys.argv[0])
        sys.exit(2)

    m = imaplib.IMAP4_SSL(hostname)
    m.login(username, getpass.getpass())
    print('Capabilities:', m.capabilities)
    print('Listing mailboxes ')
    status, data = m.list()
    print('Status:', repr(status))
    print('Data:')
    for datum in data:
        print(repr(datum))
    m.logout()

if __name__ == '__main__':
    main()
