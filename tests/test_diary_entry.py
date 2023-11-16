import pytest
from lib.diary_entry import *

"""
Given an empty title and contents
Raises an error
"""
def test_empty_title_and_contents():
    with pytest.raises(Exception) as err:
        diary_entry = DiaryEntry("", "")
    assert str(err.value) == "Diary entries must have a title or content"
"""
Given a title and contents
#format returns a formatted entry, like:
"My Title: These are the contents"
"""
def test_formatted_diary_entry():
    diary_entry = DiaryEntry("My Title", "Some contents")
    result = diary_entry.format()
    assert result == "My Title: Some contents"

"""
Given text in the diary entry
#count_words returns the number of words as int
"""

def test_number_of_words_in_diary_entry():
    diary_entry = DiaryEntry("Counting", "One two three four")
    result = diary_entry.count_words()
    assert result == 5

"""
Given WPM of 2
And a text with 2 words
#reading_time returns the estimated reading time 
for the contents
"""

# def estimated_reading_time():
#     diary_entry = DiaryEntry(10)
#     result = diary_entry.reading_time()
#     assert result == 