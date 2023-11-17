from lib.diary import *

def test_format_title_and_contents():
    diary_entry = DiaryEntry("My Title", "Some contents")
    result = diary_entry.format()
    assert result == "My Title: Some contents"

def test_number_of_words_in_diary():
    diary_entry = DiaryEntry("My Title", "Some contents")
    result = diary_entry.count_words()
    assert result == 4

def test_reading_time_in_minutes():
    diary_entry = DiaryEntry("My Title", "Some contents")
    result = diary_entry.reading_time(4)
    assert result == 1

def test_wpm_of_zero_reaises_exception():
    diary_entry = DiaryEntry("My Title", "Some contents")
    with pytest.raises(Exception) as e:
        diary_entry.reading_time(0)
    assert str(e.value) == "This is an error message"

"""
Given a contents of 4 words
And a wpm of 2
And a minutees of 1
"reading_chunk returns the first 2 words
"""
def test_reading_chunks():
    diary_entry = DiaryEntry("My Title", "Some contents by me")
    result = diary_entry.reading_chunk(2,1)
    assert result == "Some contents" 

"""
given a content of 4 words
and a wpm of 2 and 1 minute
next time "by me"
next time "by you"
"""

def test_continues_from_position():
    diary_entry = DiaryEntry("My Title", "Some contents by me by you")
    assert diary_entry.reading_chunk(2,1) == "Some contents"
    assert diary_entry.reading_chunk(2,1) == "by me"


"""
given a content of 4 words
if #reading_chunk is called repeatedly
The last chunk is the last words in the text
even if shorter than could read
The next chunk after that is at the start
next time "by me"
next time "by you"
"""
