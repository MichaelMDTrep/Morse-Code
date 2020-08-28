#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Morse Code Decoder

"Dot" – is 1 time unit long.
"Dash" – is 3 time units long.
Pause between dots and dashes in a character – is 1 time unit long.
Pause between characters inside a word – is 3 time units long.
Pause between words – is 7 time units long.
"""
__author__ = 'Michael Trepanier'

from morse_dict import MORSE_2_ASCII


def decode_bits(bits):
    m = []
    mult = 2
    bits = ("""110011001100110000001100000011111100110011111100111111
    0000000000000011001111110011111100111111000000110011
    001111110000001111110011001100000011""")

    for bit in bits:
        if bit.startswith("0000000"):
            bits.replace("0000000"*mult, " ")
        if bit.startswith("111"):
            bits.replace("111"*mult, "-")
        if bit.startswith("000"):
            bits.replace("000"*mult, " ")
        if bit.startswith("1"):
            bits.replace("1"*mult, ".")
        if bit.startswith("0"):
            bits.replace("0"*mult, "")

    return (sorted((filter(None, bits))))


def decode_morse(morse):
    """this function translates morse code into strings"""
    result = []
    for word in morse.strip().split("   "):
        ascii_word = []
        for morse_char in word.split(" "):
            ascii_word.append(MORSE_2_ASCII[morse_char])
        result.append("".join(ascii_word))
    return " ".join(result)


if __name__ == '__main__':
    hey_jude_morse = ".... . -.--   .--- ..- -.. ."
    hey_jude_bits = "11001100110011000000110000001111110011001111110011111100000000000000000000011001111110011111100111111000000110011001111110000001111110011001100000011"  # noqa

    # Be sure to run all included unit tests, not just this one.
    print("Morse Code decoder test")
    print("Part A:")
    print(f"'{hey_jude_morse}' -> {decode_morse(hey_jude_morse)}")
    print()
    print("Part B:")
    print(f"'{hey_jude_bits}' -> {decode_morse(decode_bits(hey_jude_bits))}")

    print("\nCompleted.")
