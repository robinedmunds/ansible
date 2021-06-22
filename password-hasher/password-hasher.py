#!/usr/bin/env python3
# prompts user for password, hashes password in /etc/shadow format

import getpass
from passlib.hash import sha512_crypt

print(sha512_crypt.using(rounds=5000).hash(getpass.getpass()))
