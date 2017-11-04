# -*- coding: utf-8 -*-

def box(width, height):
    for i in range(h):
    
        start = middle = end = ""

        if i == 0:
            start, middle, end = "Γ", "-", "˥"
        elif i == height - 1:
            start, middle, end = "L", "_", "┘"
        else:
            start, middle, end = "|", " ", "|"

        print(start + middle * (width - 2) + end)
