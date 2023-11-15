from lib.reading_time import *

"""
Given 200 words 
It returns 1 minute 
"""
def test_time_to_read_200_words():
    input_text = []
    for i in range(200):
        input_text.append("word")
    input_text = " ".join(input_text)
    result = estimate_reading_time(input_text)
    assert result == "1 minute"

"""
Given 400 words 
It returns 2 minute 
"""

estimate_reading_time(text) => 2 min

"""
Given 0 words 
It returns 0 minutes
"""

estimate_reading_time(text) => 2 min
def test