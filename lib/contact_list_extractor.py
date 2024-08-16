import re

class ContactListExtractor:
    def __init__(self, diary):
        # contact: list of instances of Diary 
        self.diary = diary   

    def view_numbers(self):
        # Returns
        #   List of strings of numberically correct phone numbers
        phone_numbers = set()
        for entry in self.diary.all_entries():
            found_numbers = re.findall(r"/b0[0-9]{10}/b", entry.contents)
            phone_numbers.update(found_numbers)
        return phone_numbers







 # def add_number(self, number):
    #         # Parameter:
    #         #   entry: an instance of ContactListExtractor
    #         # Side-effects:
    #         # Add number to the ContactListExtractor properties of the self object.
    #         pass