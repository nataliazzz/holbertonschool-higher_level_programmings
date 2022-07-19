#!/usr/bin/python3
"""
sends requuests and shows value
"""

from sys import argv
from urllib.request import Request, urlopen


if __name__ == "__main__":
    req = Request(argv[1])

    with urlopen(req) as res:
        headers = res.info()
        print(headers.get('X-Request-Id'))
