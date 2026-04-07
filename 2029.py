# -*- coding: utf-8 -*-

while True:
    try:
        vol = float(input())
        Diam = float(input())

        areaB = 3.14 *((Diam/2)**2)
        H = vol/areaB

        print(f"ALTURA = {H:.2f}")
        print(f"AREA = {areaB:.2f}")   
    except EOFError:
        break
