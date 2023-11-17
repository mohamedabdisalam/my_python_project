import pytest
from lib.task_tracker import *

"""
Initialise test
"""
def test_tracker_initialises():
    task = TaskTracker()
    assert isinstance(task, TaskTracker)

"""
Given a task add this 
to the task list
"""
def test_tracker_add_task():
    task = TaskTracker()
    task.add_task("Food shopping")
    actual_result = task.task_list[0]
    expected_result = "Food shopping"

    assert expected_result == actual_result


"""
Given we have list
returns that list
"""

def test_tracker_see_task():
    task = TaskTracker()
    task.add_task("Food shopping")
    actual_result = task.see_list()
    expected_result = ["Food shopping"]

    assert expected_result == actual_result

"""
"Given an empty string to add to list
raise an error "A task is required"
"""
def test_tracker_with_an_empty_string():
    task = TaskTracker()
    with pytest.raises(Exception) as e:
        task.add_task("")
    error_message = str(e.value)
    assert error_message == "A task is required"
"""
Given that the list empty
return an error message
raise Exception "You're all done with your tasks" 
"""

def test_tracker_with_an_empty_list():
    task = TaskTracker()
    with pytest.raises(Exception) as e:
        task.see_list()
    error_message = str(e.value)
    assert error_message == "You're all done with your tasks" 

"""
Given a user has marked a task
as complete, function finds that task
and pops it out of the list
"""
def test_tracker_mark_as_complete_and_remove():
    task = TaskTracker()
    task.add_task("Food shopping")
    task.add_task("Buy shampoo")
    task.remove_task("Buy shampoo")
    actual_result = task.see_list()
    expected_result = ["Food shopping"]

    assert expected_result == actual_result
