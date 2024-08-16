class ReadableEntry:
    # user facing properties:
    # readableentry: list of instances of DiaryEntry 
    
    def __init__(self, diary):
        # diary: list of instances of Diary 
        self.diary = diary
        

    def reading_chunk(self, wpm, minutes):
        longest = None
        longest_length = 0
        for entry in self.diary.all_entries():
            if self.word_count(entry.contents) > longest_length:
                if self.entry_readable(wpm, minutes, entry):
                    longest = entry
                    longest_length = self.word_count(entry.contents)
        return longest
        
            
    def entry_readable(self, wpm, minutes, entry):
        length_readable = wpm * minutes
        return self.word_count(entry.contents) <= length_readable
            

    def word_count(self, string):
        return len(string.split(" "))