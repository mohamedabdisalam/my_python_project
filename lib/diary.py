import pytest
class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.bookmark = 0

    def format(self):
        return f"{self.title}: {self.contents}"

    def count_words(self):
        return len(self.format().split())

    def reading_time(self, wpm):
        if wpm == 0:
            raise Exception("This is an error message")
        return len(self.format().split()) / wpm

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
    
        words_to_show = wpm * minutes
        words = self.contents.split()
        if self.bookmark >= len(words):
            self.bookmark = 0
        chunk_start = self.bookmark
        chunk_end = self.bookmark + words_to_show
        chunk = words[chunk_start:chunk_end]
        self.bookmark = chunk_end
        return " ".join(chunk)