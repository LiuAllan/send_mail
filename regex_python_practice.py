#!/usr/bin/python3

import re

n = "1000000123"
print("Before =", n)

n = re.sub(r"(?<=\d)(?=(\d{3})+$)", ",", n)
print("After =", n)
