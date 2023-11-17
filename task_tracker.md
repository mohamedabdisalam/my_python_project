# Class Task Tracker

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

class TaskTracker:
    task: string

    def __init__(self):   
        #List of tasks kept here
        # Side effects:
        #   Sets the name property of the self object
        pass # No code here yet

    def add_task(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   add that task to a list
        # Side-effects
        #   none
        pass # No code here yet

    def see_tasks(self):
        # Parameters:
        #   None
        # Returns:
        #   list of current tasks
        # Side-effects
        #   none
        pass # No code here yet

    def remove_task(self, task):
        # Parameters:
        #   Task
        # Returns:
        #   None
        # Side-effects
        #   Removes task from list
        pass # No code here yet

class MusicTracker:
    song_title: string

    def __init__(self):
        #List of song kept here
        # Side effects:
        #   Sets the name property of the self object
        pass # No code here yet
    
    def add_song(self, song):
        # Parameters:
        #   song: string representing a single song
        # Returns:
        #   add that song to a list
        # Side-effects
        #   none
        pass # No code here yet
    
    def see_songs(self):
        # Parameters:
        #   None
        # Returns:
        #   list of listened to song
        # Side-effects
        #   none
        pass # No code here yet

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

"""
Given a task add this 
to the task list
"""
task = TaskTracker()
task.add("Food shopping")
task.add() # => "Food shopping added to list"

"""
Given we have list
returns that list
"""
task = TaskTracker()
task.see_tasks()
task.see_tasks() => "Food shopping"

"""
"Given an empty string to add to list
raise an error "A task is required"
"""
task = TaskTracker()
task.add("")
task.add() => error "A task is required"

"""
Given that the list empty
return an error message
raise Exception "You're all done with your tasks" 
"""
task = TaskTracker()
task.see_list()
task.see_list() => error "You're all done with your tasks" 

"""
Given a task to remove
remove task

"""
task = TaskTracker()
task.remove_task()
task.see_list() => list without task 

"""
Test initiailisation

music = MusicTracker()
isinstance(music, MusicTracker)

"""
Given a song  
add to song list

music = MusicTracker()
music.add_song()
list --> updated list

""""
Given we have a list of great songs
return the list

music = MusicTracker()
music.see_songs()
returns list to user

"""
Exception
Given a song is not added
return error message

music = MusicTracker()
music.add_song()
error message

"""
Exception
If list is empty
return error message

music = MusicTracker()
music.see_songs()
Error message 'You haven't listened to some great music yet!'


## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._


