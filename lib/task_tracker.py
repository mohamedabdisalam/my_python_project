class TaskTracker():

    def __init__(self):
        self.task_list = []

    def add_task(self, task):
        if task == "":
            raise Exception("A task is required")
        self.task_list.append(task)
    
    def see_list(self):
        if self.task_list == []:
            raise Exception("You're all done with your tasks" )
        return self.task_list

    def remove_task(self, task):
        loc = self.task_list.index(task)
        self.task_list.pop(loc)

