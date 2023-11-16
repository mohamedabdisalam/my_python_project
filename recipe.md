
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
Function works

Challenge

1. Describe the problem

As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.

2. Design the function signature

def check_todo(text):
""" Check if a text includes the string #TODO

Parameters:
    text: a string

    Returns: 
        True if conditions are met or false otherwise
        Boolean

    Side effects:
        No known side effects at this point 
"""
pass

3. Create Examples as Tests
"""
Happy path 
Checks for #TODO and returns True.
"""
Call check_todo with "This is a task #TODO"
Pass

Call check_todo with "This is a task"
Fail

4. Implement the behaviour

1. Describe the problem

As a user
So that I can improve my grammar
I want to verify that a text starts 
with a capital letter and ends 
with a suitable sentence-ending punctuation mark.

2. Design the function signature

def check_grammar(text):
""" Confirm if a text starts with a capital letter and ends with a punctuation mark

Parameters:
    text: a string

    Returns: 
        True if conditions are met or false otherwise
        Boolean

    Side effects:
        No known side effects at this point 
"""
pass

3. Create Examples as Tests
"""
Happy path 
Checks for Capital letter and a suitable punctuation mark - !?.
"""
Call check_grammar with "This is a sentence."
Pass

Call check_grammar with "This is a sentence,"

Call check_grammar with "this is a sentence!"

4. Implement the behaviour