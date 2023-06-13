#!/usr/bin/python3
"""
function that prints a text with 2 new lines after
each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    function that prints a text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    phrase = ""
    for element in text:
        if element in [".", "?", ":"]:
            phrase += element
            print(phrase.strip())
            print()
            phrase = ""
        else:
            phrase += element
    print(phrase.strip(), end="")
