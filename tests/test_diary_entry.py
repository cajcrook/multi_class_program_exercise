from lib.diary_entry import DiaryEntry

"""
@DiaryEntry
__init__
Test DiaryEntry is constructed correctly with title and content
"""
def test_entry_to_return_title_content():
    diaryentry = DiaryEntry("Title_1", "Content_1")
    assert diaryentry.title == "Title_1"
    assert diaryentry.contents == "Content_1"
