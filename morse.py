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
__author__ = 'Michael Trepanier got help from piero'

from morse_dict import MORSE_2_ASCII


def decode_bits(bits):
    """ strip off leading and trailing zeros """
    bits = bits.strip("0")

    """ check multipliers starting with 1 and going up """
    m = 0
    if (bits.startswith("101") or bits.startswith("10001")):
        m = 1
    elif (bits.startswith("110011") or bits.startswith("1100000011")):
        m = 2
    elif (bits.startswith("111000111") or bits.startswith("111000000000111")):
        m = 3
    elif (bits.startswith("111100001111") or
          bits.startswith("11110000000000001111")):
        m = 4
    elif (bits.startswith("111110000011111") or
          bits.startswith("1111100000000000000011111")):
        m = 5
    elif (bits.startswith("111111000000111111") or
          bits.startswith("111111000000000000000000111111")):
        m = 6
    elif (bits.startswith("11101") or bits.startswith("1110001")):
        m = 1
    elif (bits.startswith("1111110011") or bits.startswith("11111100000011")):
        m = 2
    elif (bits.startswith("111111111000111") or
          bits.startswith("111111111000000000111")):
        m = 3
    elif (bits.startswith("11111111111100001111") or
          bits.startswith("1111111111110000000000001111")):
        m = 4
    elif (bits.startswith("1111111111111110000011111") or
          bits.startswith("11111111111111100000000000000011111")):
        m = 5
    elif (bits.startswith("111111111111111111000000111111") or
          bits.startswith("111111111111111111000000000000000000111111")):
        m = 6
    else:
        m = len(bits)

    print('multiplier =', m)

    """ initialize separators """
    word_sep = "".join(['0']*7*m)
    letter_sep = "".join(['0']*3*m)
    key_sep = "".join(['0']*m)
    dot = "".join(['1']*m)
    dash = "".join(['1']*3*m)

    """ get the incoming words """
    words_in = bits.split(word_sep)
    words_out = []
    for word in words_in:
        """ split the incoming words in to letters """
        letters_in = word.strip("0").split(letter_sep)
        letters_out = []
        for letter in letters_in:
            """ split the incoming letters in to codes """
            codes_in = letter.split(key_sep)
            codes_out = []
            for code in codes_in:
                if (code == dot):
                    codes_out.append('.')
                elif (code == dash):
                    codes_out.append('-')
                else:
                    print('error ', code)
            """ join the outgoing codes to make letters """
            letters_out.append("".join(codes_out))
        """ join the outgoing letter to make words """
        words_out.append(" ".join(letters_out))

    print('words out ', words_out)
    """ return the outgoing words after joining them """
    return("   ".join(words_out))


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
