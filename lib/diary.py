
class Diary:
    # user facing properties:
    # diary entries: list of instances of DiaryEntries 

    def __init__(self):
        self.entries = []   

    def add_entry(self, entry):
        # Parameter:
        #   entry: an instance of DiaryEntries
        # Side-effects:
        # Add entry to the diary entry properties of the self object.
        self.entries.append(entry)
    
    def all_entries(self):
        # Returns:
        # list of all diary entries
        return self.entries