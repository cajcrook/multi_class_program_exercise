from lib.readable_entry import ReadableEntry
from lib.diary_entry import DiaryEntry
from lib.diary import Diary

"""
ReadableEntry
reading_chunk()
When I add one entry that fits the time
2 wpm, 3 mins = 6 words
"""
def test_add_one_acceptable_entry():
    diary = Diary()
    entry_1 = DiaryEntry("Title_1", "One two three four five six")
    diary.add_entry(entry_1)
    extractor = ReadableEntry(diary)
    assert extractor.reading_chunk(wpm=2, minutes=3) == (entry_1)
    
"""
ReadableEntry
reading_chunk()
When I add one entry that is too long for critera
Returns None
2 wpm, 3 mins = 6 words
"""
def test_return_none_reading_chunk_too_long():
    diary = Diary()
    entry_1 = DiaryEntry("Title_1", "One two three four five six seven")
    diary.add_entry(entry_1)
    extractor = ReadableEntry(diary)
    assert extractor.reading_chunk(wpm=2, minutes=3) == None
    
"""
ReadableEntry
reading_chunk()
When I add two entries and one is too long for critera
Returns readable one
2 wpm, 3 mins = 6 words
"""
def test_return_best_reading_chunk_based_on_criteria():
    diary = Diary()
    entry_1 = DiaryEntry("Title_1", "One two three four five six")
    entry_2 = DiaryEntry("Title_2", "One two three four five six seven")
    diary.add_entry(entry_1)
    diary.add_entry(entry_2)
    extractor = ReadableEntry(diary)
    assert extractor.reading_chunk(wpm=2, minutes=3) == entry_1

"""
ReadableEntry
reading_chunk()
When I add multiple entries and one is readable
Returns longest readable one
2 wpm, 3 mins = 6 words
"""
def test_add_multiple_return_reading_chunk_based_on_criteria():
    diary = Diary()
    entry_1 = DiaryEntry("Title_1", "One two three four five six seven")
    entry_2 = DiaryEntry("Title_2", "One two three four five six seven eight")
    entry_3 = DiaryEntry("Title_3", "One two three four five six")
    entry_4 = DiaryEntry("Title_4", "One two three")
    entry_5 = DiaryEntry("Title_5", "One two three four five six seven")
    diary.add_entry(entry_1)
    diary.add_entry(entry_2)
    diary.add_entry(entry_3)
    diary.add_entry(entry_4)
    diary.add_entry(entry_5)
    extractor = ReadableEntry(diary)
    assert extractor.reading_chunk(wpm=2, minutes=3) == entry_3

"""
ReadableEntry
reading_chunk()
When I add no diary entries
Returns None
2 wpm, 3 mins = 6 words
"""
def test_return_none_no_entries():
    diary = Diary()
    extractor = ReadableEntry(diary)
    assert extractor.reading_chunk(wpm=2, minutes=3) == None

    