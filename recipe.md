
1. Describing the problem
As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

2. Design the function signature

def estimate_reading_time(text):
""" State the estimated reading time based on the length of the text

Parameters:
    text: a string

    Returns: 
        length of the text, float 

    Side effects:
        No known side effects at this point 
"""
pass

3. Create Examples as Tests

"""
Given 200 words 
It returns 1 minute 
"""

estimate_reading_time(text) => 1 min

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


4. Implement the behaviour

