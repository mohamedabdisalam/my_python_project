from lib.check_todo import *

"""
Happy path 
Checks for #TODO and returns True.
Call check_todo with "This is a task #TODO"
"""


def test_todo_in_text():
    result = check_todo("This is a task #TODO")
    assert result == True


""""""
# Call check_todo with "This is a task"
# Fail
""""""

def test_todo_not_in_text():
    result = check_todo("This is a task")
    assert result == False

"""
Checks for #TODO when there
all tasks include todo
"""

def test_todo_in_multiple_texts_with_all_inc_TODO():
    result = check_todo("This is a task #TODO")
    result = check_todo("This is a task #TODO")
    result = check_todo("This is a task #TODO")
    assert result == True

"""
Checks for #TODO when multiple tasks
do not include £TODO
"""

def test_todo_in_multiple_texts_none_inc_TODO():
    result = check_todo("This is a task")
    result = check_todo("This is a task")
    result = check_todo("This is a task")
    assert result == False

"""
Checks for #TODO when some tasks
include £TODO
"""

def test_todo_when_some_text_inc_TODO():
    result = check_todo("This is a task")
    result = check_todo("This is a task #TODO")
    result = check_todo("This is a task")
    assert result == True