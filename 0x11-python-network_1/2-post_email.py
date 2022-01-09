#!/usr/bin/python3
""" Made by Christian """

import urllib.parse as parse
import urllib.request as respuesta
from sys import argv

if __name__ == "__main__":
    dict = {'email': argv[2]}
    elemento = parse.urlencode(dict).encode('utf-8')
    data = respuesta.Request(argv[1], elemento)
    with respuesta.urlopen(data) as res:
        print(res.read().decode('utf-8'))
