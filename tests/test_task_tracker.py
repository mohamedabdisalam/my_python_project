import pytest
from lib.task_tracker import *

"""
Initialise test
"""
def test_tracker_task_initialises():
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

# Test initiailisation

def test_tracker_music_initialises():
    music = MusicTracker()
    assert isinstance(music, MusicTracker)

# Given a song  
# add to song list

def test_tracker_music_add_song():
    music = MusicTracker()
    music.add_song("Heads, shoulders, knees and toes")
    actual_result = music.song_list[0]
    expected_result = "Heads, shoulders, knees and toes"

    assert expected_result == actual_result

# """"
# Given we have a list of great songs
# return the list

def test_tracker_music_see_songs():
    music = MusicTracker()
    music.add_song("Heads, shoulders, knees and toes")
    actual_result = music.see_songs()
    expected_result = ["Heads, shoulders, knees and toes"]

    assert expected_result == actual_result


"""
Exception
Given a song is not added
return error message

"""
def test_tracker_music_with_an_empty_string():
    music = MusicTracker()
    with pytest.raises(Exception) as e:
        music.add_song("")
    error_message = str(e.value)
    assert error_message == "Please add a song"

"""
Exception
If list is empty
return error message

music = MusicTracker()
music.see_songs()
Error message 'You haven't listened to some great music yet!'
"""
def test_tracker_music_with_an_empty_list():
    music = MusicTracker()
    with pytest.raises(Exception) as e:
        music.see_songs()
    error_message = str(e.value)
    assert error_message == "You haven't listened to some great music yet!"