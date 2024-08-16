from lib.task_list import TaskList

"""
@TaskList
__init__
Initially TaskList has no incomplete tasks
"""
def test_initial_incomplete_tasklist_is_empty():
    tasklist = TaskList()
    assert tasklist.incomplete() == [] 
    
"""
@TaskList
__init__
Initially TaskList has no complete tasks
"""
def test_initial_complete_tasklist_is_empty():
    tasklist = TaskList()
    assert tasklist.complete() == [] 

# """
# @TaskList
# incomplete
# Test that a list of incomplete tasks is returned
# """
# def test_incomplete_tasks_returned():
#     tasklist = TaskList()
#     task_1 = TaskList("My first task", False)
#     task_2 = TaskList("My second task", False)
#     task_3 = TaskList("My third task", True)
#     tasklist.add_task(task_1)
#     tasklist.add_task(task_2)
#     task_3.mark_complete()
#     assert tasklist.incomplete() == ["My first task", "My second task"]

# """
# @TaskList
# complete
# Test that a list of complete tasks is returned
# """
# def test_complete_tasks_returned():
#     tasklist = TaskList()
#     task_1 = TaskList("My first task", False)
#     task_2 = TaskList("My second task", True)
#     task_3 = TaskList("My third task", True)
#     tasklist.add_task(task_1)
#     task_2.mark_complete()
#     task_3.mark_complete()
#     assert tasklist.complete() == ["My second task", "My third task"]




