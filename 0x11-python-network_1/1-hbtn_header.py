#!/usr/bin/python3
""" Made by Christian """
import urllib.request as llamada
from sys import argv

if __name__ == "__main__":
    datos = llamada.Request(argv[1])
    with llamada.urlopen(datos) as res:
        print(res.getheader('X-Request-Id'))
