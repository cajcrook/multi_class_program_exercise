from lib.task import Task
"""
Task contructs title
"""
def test_task_constructs_title():
    task = Task("Task_1")
    assert task.title == "Task_1"


"""
Task newly constructs tasks are not complete
"""
def test_new_tasks_not_complete():
    task = Task("Task_1")
    assert task.complete == False


"""
When I mark task as complete 
It is show in complete property
"""
def test_task_complpete():
    task = Task("Task_2")
    task.mark_complete()
    assert task.complete == True


# """
# Task
# __init__
# Test Task is initialised correctly
# """
# def test_task_to_return_task_and_boolean():
#     task = Task("My first task", False)
#     assert task.task == "My first task"
#     assert task.status == False

# """
# Task
# mark_complete
# Test to change  status to True (complete)
# """
# def test_update_status():
#      task = Task("My first task", False)
#     assert task.task == "My first task"
#     assert task.status == True