class Task:
    # Public Properties:
    #   task: a string
    #   complete: a boolean (true = complete)

    def __init__(self, title):
        # Parameters:
        #   task: a string representing the task to be done
        #   boolean: reflecting status of task
        # Side-effects:
        #   Sets the task property
        #   Sets the complete property to False
        self.title = title
        self.complete = False


    def mark_complete(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Sets the complete property to True
        self.complete = True
