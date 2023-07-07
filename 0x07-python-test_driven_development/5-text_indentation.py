#!/usr/bin/python3
"""
function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""
def text_indentation(text):
    """
    function that prints a text with 2 new lines
    after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    lenght = 0
    while text[lenght] == ' ' and lenght < len(text):
        lenght += 1
    while lenght < len(text):
        print(text[lenght], end="")
        if text[lenght] in punctuation:
            print("\n")
        lenght += 1
        while lenght < len(text) and text[lenght] == ' ':
            lenght += 1                                                                                                     continue
        lenght += 1
