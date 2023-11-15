from lib.make_snippet import *

"""
If given empty string
It returns empty string
"""
def test_empty_string():
    result = make_snippet("")
    assert result == ""
"""
A function called make_snippet that takes a string
as an argument and returns the first five words 
"""

def test_first_four_words():
    result = make_snippet("one two three four")
    assert result == "one two three four"

"""
If more than 5 characters returns
string + '...' if there are more than that.
"""
def test_first_five_words():
    result = make_snippet("one two three four five")
    assert result == "one two three four five"

def test_first_six_words():
    result = make_snippet("one two three four five six")
    assert result == "one two three four five" + "..."