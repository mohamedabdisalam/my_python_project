from lib.count_words import *

"""
A function called count_words that 
takes a string as an argument and 
returns the number of words in that string.
"""

"""
Takes empty string
"""

def test_empty_string():
    result = count_words("")
    assert result == 1

def test_length_of_single_string():
    result = count_words("one two")
    assert result == 2

def test_length_of_multiple_string():
    result = count_words("one two three")
    assert result == 3