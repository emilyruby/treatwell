# -*- coding: utf-8 -*-


def box(width, height):

    if width <= 1 or height <= 1:
        return

    result = ''

    for i in range(height):

        start = middle = end = ""

        if i == 0:
            # first row
            start, middle, end = "Γ", "-", "˥"
        elif i == height - 1:
            # last row
            start, middle, end = "L", "_", "┘"
        else:
            # anywhere but the first or last row
            start, middle, end = "|", " ", "|"

        # draw the box with the start character, the appropriate number of
        # middle characters, and the end character.

        result += (start + middle * (width - 2) + end) + '\n'

    return result
