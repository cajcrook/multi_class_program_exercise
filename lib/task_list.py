class TaskList:
        # user facing properties:
        # task: list of instances of Task
    
    def __init__(self):
        self.tasks = []   

    def add_task(self, task):
        # Parameter
        #   task: string
        # Side-effects:
            # Adds task to the tasklist properties of the self object.
        self.tasks.append(task)

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        return [
            task for task in self.tasks
            if not task.complete
        ]
        
    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        return [
            task for task in self.tasks
            if task.complete
        ]