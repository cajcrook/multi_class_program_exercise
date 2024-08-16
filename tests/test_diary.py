from lib.diary import Diary

"""
@Diary
__init__
Initially Diary has no entries
"""
def test_initial_diary_is_empty():
    diary = Diary()
    assert diary.all_entries() == [] 
