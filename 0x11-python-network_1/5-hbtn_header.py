#!/usr/bin/python3
"""This script takes in a URL, sends a request to the
URL and displays the value of the X-Request-Id
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
