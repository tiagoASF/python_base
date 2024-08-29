#!/usr/bin/env python3

"""Imprime a tabuada do 1 ao 10.

Tabuada do 1
1
2
3
...
--------------
Tabuada do 2
2
4
6
...
--------------

"""

__version__ = "0.1.0"
__author__ = "Tiago Fialho"


base = list(range(1, 11))

for numero in base:
    print(f"Tabuada do {numero}")
    for outro_numero in base:
        print(f"{numero} X {outro_numero} = {numero * outro_numero}")
    print("---" * 10)
