from lib.diary import Diary
from lib.diary_entry import DiaryEntry

"""
@Diary
all_entries
Test that when we add 2 entries, they appear in the all_entries
"""
def test_add_two_entries_to_diary():
    diary = Diary()
    entry_1 = DiaryEntry("Title_1", "Contents_1")
    entry_2 = DiaryEntry("Title_2", "Contents_2")
    diary.add_entry(entry_1)
    diary.add_entry(entry_2)
    assert diary.all_entries() == [entry_1, entry_2]

