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
        self.title = title
        self.contents = contents