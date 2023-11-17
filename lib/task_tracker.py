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

class MusicTracker():

    def __init__(self):
        self.song_list = []

    def add_song(self, song):
        if song == "":
            raise Exception("Please add a song")
        self.song_list.append(song)

    def see_songs(self):
        if self.song_list == []:
            raise Exception("You haven't listened to some great music yet!")
        return self.song_list