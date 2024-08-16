# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries

# Nouns
Diary
    Past Diary
    Diary entries
        Time
        Speed
Task List
    Tasks
Contact List
    Contacts

# Verbs
Record
Keep
Reflect
Read
Select
Keep




## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```python
class Diary:
    # user facing properties:
    # diary entries: list of instances of DiaryEntries 

    def __init__(self):
        pass   

        def add_entry(self, entry):
            # Parameter:
            #   entry: an instance of DiaryEntries
            # Side-effects:
            # Add entry to the diary entry properties of the self object.
            pass
        
        def all_entries(self):
            # Returns:
            # list of all diary entries
--------------------------------------------
        # def search_by_title(self, title):
        #     # Parameters
        #     #    title: string
        #     # Returns
        #     # A list showing the content for entries containing title.
        #     pass
--------------------------------------------

class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string
 
    def __init__(self, title, contents):
        # Parameter
        #   title: string 
        #   contents: string
        # Side-effects:
        #   sets the title and content properties
        pass

class TaskList:
        # user facing properties:
        # task: list of instances of Task
    
    def __init__(self):
        pass   

    def add_task(self, task):
        # Parameter
        #   task: string
        # Side-effects:
            # Adds task to the tasklist properties of the self object.
        pass

    def all_tasks(self):
        # Returns
        #   A list showing all tasks
        pass

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        pass
        
    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        pass

class Task:
    # Public Properties:
    #   task: a string
    #   complete: a boolean (true = complete)

    def __init__(self, task, status):
        # Parameters:
        #   task: a string representing the task to be done
        #   boolean: reflecting status of task
        # Side-effects:
        #   Sets the task property
        #   Sets the complete property to False
        pass

    def mark_complete(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Sets the complete property to True
        pass


class ContactListExtractor:

    def __init__(self, contact):
        # contact: list of instances of Diary 
        pass   

    # def add_number(self, number):
    #         # Parameter:
    #         #   entry: an instance of ContactListExtractor
    #         # Side-effects:
    #         # Add number to the ContactListExtractor properties of the self object.
    #         pass

    def view_numbers():
        # Returns
        #   List of strings of numberically correct phone numbers


class ReadableEntry:
    # user facing properties:
    # readableentry: list of instances of DiaryEntry 
    
    def __init__(self, diary):
        # diary: list of instances of Diary 
        pass   

    def reading_chunk(self, wpm, minutes):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.
        pass


_Also design the interface of each class in more detail._

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

___INTEGRATED TESTS___

"""
@Diary
all_entries
Test that when we add an entry it appears in the all_entries
"""
def test_add_entry_to_diary():
    diary = Diary()
    entry_1 = DiaryEntry("Title_1", "Contents_1")
    diary.add(entry_1)
    assert diary.all_entries

"""
@Diary
all_entries
Test that when we add 2 entries, they appear in the all_entries
"""
def test_add_two_entries_to_diary():
    diary = Diary()
    entry_1 = DiaryEntry("Title_1", "Contents_1")
    entry_2 = DiaryEntry("Title_2", "Contents_2")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.all_entries

"""
@TaskList
all_tasks 
add_tasks
Test that when we add a task it appears in the all_tasks
"""
def test_add_task_to_tasklist():
    tasklist = TaskList()
    task_1 = TaskList("My first task", False)
    tasklist.add_task(task_1)
    assert tasklist.all_tasks

"""
@TaskList
all_tasks 
add_tasks
Test that when we add 2 tasks, they appear in the all_tasks
"""
def test_add_two_tasks_to_tasklist():
    tasklist = TaskList()
    task_1 = TaskList("My first task", False)
    task_2 = TaskList("My second task", False)
    tasklist.add_task(task_1)
    tasklist.add_task(task_2)
    assert tasklist.all_tasks

"""
ContactListExtractor 
__init__
Test ContactListExtractor is initialised correctl. 11 digit, string
"""
def test_contact_list_extractor():
    contactlistextractor = ContactListExtractor("07990735837")
    assert contactlistextractor.contact == "07990735837"

"""
ContactListExtractor 
__init__
Test that initially ContactListExtractor is empty
"""
def test_contact_list_is_empty():
    contactlistextractor = ContactListExtractor()
    assert contactlistextractor.view_numbers() == []

"""
@ContactListExtractor
when I call ContactListExtractor
I get a list of all phone numbers from diary entries
"""
def test_extract_multiple_numbers_from_diary():
    diary = Diary()
    entry_1 = DiaryEntry("Title_1", "Person_1 is 07990735837")
    entry_2 = DiaryEntry("Title_2", "Person_2 is 01234567891 and 11111111111")
    entry_3 = DiaryEntry("Title_3", "Person_3")
    diary.add(entry_1)
    diary.add(entry_1)
    diary.add(entry_3)
    extractor = ContactListExtractor(diary)
    extractor.view_numbers() = ["07990735837", "01234567891", "11111111111"]

"""
@ContactListExtractor
when I call ContactListExtractor
I get a list of all phone numbers from diary entries
Ignoring invalid numbers
"""
def test_extract_multiple_numbers_from_diary_igoring_invalid():
    diary = Diary()
    entry_1 = DiaryEntry("Title_1", "Person_1 is 07990735837")
    entry_2 = DiaryEntry("Title_2", "Person_2 is 012345678 and 11111111")
    entry_3 = DiaryEntry("Title_3", "Person_3 is 33334455667 and 333")
    diary.add(entry_1)
    diary.add(entry_1)
    diary.add(entry_3)
    extractor = ContactListExtractor(diary)
    extractor.view_numbers() = ["07990735837", "33334455667"]

"""
@ContactListExtractor
when I call ContactListExtractor
I get a list of all phone numbers from diary entries
Ignoring duplicate numbers
"""
def test_extract_multiple_numbers_from_diary_igoring_invalid():
    diary = Diary()
    entry_1 = DiaryEntry("Title_1", "Person_1 is 07990735837")
    entry_2 = DiaryEntry("Title_2", "Person_2 is 07990735837 and 11111111")
    entry_3 = DiaryEntry("Title_3", "Person_3 is 33334455667 and 333")
    diary.add(entry_1)
    diary.add(entry_1)
    diary.add(entry_3)
    extractor = ContactListExtractor(diary)
    extractor.view_numbers() = ["07990735837", "33334455667"]

"""
@ContactListExtractor
When I add no diary entries
when I call ContactListExtractor 
It returns an empty list
"""
def test_no_entries_gives_entry_list():
    diary = Diary()
    extractor = ContactListExtractor(diary)
    extractor.view_numbers() = []

# """
# ReadableEntry
# __init__
# Test that initially ReadableEntry is empty
# """
# def test_readable_entry_is_empty():
#     readableentry = ReadableEntry()
#     assert readableentry.view_numbers() == ()

"""
ReadableEntry
reading_chunk()
Test to return a chunk of content based on critera (wpm * minutes),
2 wpm, 3 mins = 6 words
"""
def test_return_reading_chunk_based_on_criteria():
    entry_1 = DiaryEntry("Title_1", "One two three four five six")
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
    entry_1 = DiaryEntry("Title_1", "One two three four five six ")
    entry_2 = DiaryEntry("Title_2", "One two three four five six seven")
    diary.add_entry(entry_1)
    diary.add_entry(entry_2)
    extractor = ReadableEntry(diary)
    assert extractor.reading_chunk(wpm=2, minutes=3) == (entry_2)

"""
ReadableEntry
reading_chunk()
When I add multiple entries and one is readable
Returns longest readable one
2 wpm, 3 mins = 6 words
"""
def test_add_multiple_return_reading_chunk_based_on_criteria():
    entry_1 = DiaryEntry("Title_1", "One two three four five")
    entry_2 = DiaryEntry("Title_2", "One two three four five six")
    entry_3 = DiaryEntry("Title_2", "One two three four five six seven eight")
    diary.add_entry(entry_1)
    diary.add_entry(entry_2)
    diary.add_entry(entry_3)
    extractor = ReadableEntry(diary)
    assert extractor.reading_chunk(wpm=2, minutes=3) == (entry_2)

"""
ReadableEntry
reading_chunk()
When I add no diary entries
Returns None
2 wpm, 3 mins = 6 words
"""
def test_return_none_no_entries():
    extractor = ReadableEntry(diary)
    assert extractor.reading_chunk(wpm=2, minutes=3) == None

    



-------------------------------------------------------------------------------------------------
## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

_______UNIT TESTS______

"""
@Diary
__init__
Initially Diary has no entries
"""
def test_initial_diary_is_empty():
    diary = Diary()
    assert diary.all_entries == [] 

"""
@DiaryEntry
__init__
Test DiaryEntry is initialised correctly
"""
def test_entry_to_return_title_content():
    diaryentry = DiaryEntry("Title_1", "Content_1")
    assert diaryentry.title == "Title_1"
    assert diaryentry.content == "Content_1"

"""
@TaskList
__init__
Initially TaskList has no tasks
"""
def test_initial_tasklist_is_empty():
    tasklist = TaskList()
    assert tasklist.all_tasks == [] 

"""
Task
__init__
Test Task is initialised correctly
"""
def test_task_to_return_task_and_boolean():
    task = Task("My first task", False)
    assert task.task == "My first task"
    assert task.status == False

"""
Task
mark_complete
Test to change  status to True (complete)
"""
def test_update_status():
     task = Task("My first task", False)
    assert task.task == "My first task"
    assert task.status == True

"""
@TaskList
incomplete
Test that a list of incomplete tasks is returned
"""
def test_incomplete_tasks_returned():
    tasklist = TaskList()
    task_1 = TaskList("My first task", False)
    task_2 = TaskList("My second task", False)
    task_3 = TaskList("My third task", True)
    tasklist.add_task(task_1)
    tasklist.add_task(task_2)
    task_3.mark_complete()
    assert tasklist.incomplete() == ["My first task", "My second task"]

"""
@TaskList
complete
Test that a list of complete tasks is returned
"""
def test_complete_tasks_returned():
    tasklist = TaskList()
    task_1 = TaskList("My first task", False)
    task_2 = TaskList("My second task", True)
    task_3 = TaskList("My third task", True)
    tasklist.add_task(task_1)
    task_2.mark_complete()
    task_3.mark_complete()
    assert tasklist.complete() == ["My second task", "My third task"]




_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour.


