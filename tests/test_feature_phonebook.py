from lib.diary import Diary
from lib.diary_entry import DiaryEntry
from lib.contact_list_extractor import ContactListExtractor

"""
@ContactListExtractor
when I call ContactListExtractor
I get a list of all phone numbers from diary entries
"""
def test_extract_multiple_numbers_from_diary():
    diary = Diary()
    entry_1 = DiaryEntry("Title_1", "Person_1 is 07990735837")
    entry_2 = DiaryEntry("Title_2", "Person_2 is 0799073588")
    entry_3 = DiaryEntry("Title_3", "Person_3")
    diary.add_entry(entry_1)
    diary.add_entry(entry_1)
    diary.add_entry(entry_3)
    extractor = ContactListExtractor(diary)
    assert extractor.view_numbers() == set()


"""
@ContactListExtractor
when I call ContactListExtractor
I get a list of all phone numbers from diary entries
Ignoring duplicate numbers
"""
def test_extract_multiple_numbers_from_diary_igoring_duplicates():
    diary = Diary()
    entry_1 = DiaryEntry("Title_1", "Person_1 is 07990735837")
    entry_2 = DiaryEntry("Title_2", "Person_2 is 07990735839 and 07990735837")
    diary.add_entry(entry_1)
    diary.add_entry(entry_2)
    extractor = ContactListExtractor(diary)
    assert extractor.view_numbers() == set()


"""
@ContactListExtractor
when I call ContactListExtractor
I get a list of all phone numbers from diary entries
Ignoring invalid numbers
"""
def test_extract_multiple_numbers_from_diary_igoring_invalid():
    diary = Diary()
    entry_1 = DiaryEntry("Title_1", "Person_1 is 07990735837 and 079907358387 and07990735837")
    diary.add_entry(entry_1)
    extractor = ContactListExtractor(diary)
    assert extractor.view_numbers() == set()

"""
@ContactListExtractor
When I add no diary entries
when I call ContactListExtractor 
It returns an empty list
"""
def test_no_entries_returns_entry_list():
    diary = Diary()
    extractor = ContactListExtractor(diary)
    assert extractor.view_numbers() == set()


    

# """
# ContactListExtractor 
# __init__
# Test ContactListExtractor is initialised correctl. 11 digit, string
# """
# def test_contact_list_extractor():
#     contactlistextractor = ContactListExtractor("07990735837")
#     assert contactlistextractor.contact == "07990735837"

# """
# ContactListExtractor 
# __init__
# Test that initially ContactListExtractor is empty
# """
# def test_contact_list_is_empty():
#     contactlistextractor = ContactListExtractor()
#     assert contactlistextractor.view_numbers() == []

