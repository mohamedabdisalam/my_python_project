# Class Task Tracker

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

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


## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._


