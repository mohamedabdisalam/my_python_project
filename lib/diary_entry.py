class DiaryEntry:
    def __init__(self, title, contents):
        if title == "" or contents == "":
            raise Exception("Diary entries must have a title or content")
        self.title  = title
        self.contents = contents
        self.bookmark = 0


    def format(self):
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        return f"{self.title}: {self.contents}"

    def count_words(self):
        # Returns:
        #   int: the number of words in the diary entry
        words = self.format().split()
        return len(words)
        

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        estimate = int(self.count_words() / wpm)
        return estimate 

    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        if self.bookmark >= self.count_words() - 1:
            self.bookmark = 0
        words_to_show = wpm * minutes
        words = self.contents.split()
        # if self.bookmark >= len(words):
            # self.bookmark = 0
        chunk = words[self.bookmark:self.bookmark + words_to_show]
        string_chunk = ' '.join(chunk) 
        self.bookmark += words_to_show
        return string_chunk 

        # if i'm at the end start agian