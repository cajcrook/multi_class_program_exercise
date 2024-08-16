from lib.task import Task
from lib.task_list import TaskList

"""
@Tasklist
When I add multiple tasks
and dont mark any as complete
all incomplete lists them out as they were added
"""
def test_list_multi_tasks_all_incomplete():
    tasklist = TaskList()
    task_1 = Task("Task_1")
    task_2 = Task("Task_2")
    task_3 = Task("Task_3")
    tasklist.add_task(task_1)
    tasklist.add_task(task_2)
    tasklist.add_task(task_3)
    assert tasklist.incomplete() == [task_1, task_2, task_3]

"""
@Tasklist
When I add multiple tasks
mark one as complete 
all incomplete lists them out as they were added
"""
def test_mark_one_test_as_complete_then_removed_from_incomplete_list():
    tasklist = TaskList()
    task_1 = Task("Task_1")
    task_2 = Task("Task_2")
    task_3 = Task("Task_3")
    tasklist.add_task(task_1)
    tasklist.add_task(task_2)
    tasklist.add_task(task_3)
    task_2.mark_complete()
    assert tasklist.incomplete() == [task_1, task_3]

"""
@Tasklist
When I add multiple tasks
mark one as complete 
complpete task present in complete list
"""
def test_mark_one_test_as_complete_visible_in_complete_list():
    tasklist = TaskList()
    task_1 = Task("Task_1")
    task_2 = Task("Task_2")
    task_3 = Task("Task_3")
    tasklist.add_task(task_1)
    tasklist.add_task(task_2)
    tasklist.add_task(task_3)
    task_2.mark_complete()
    assert tasklist.complete() == [task_2]







# """
# @TaskList
# all_tasks 
# add_tasks
# Test that when we add 2 tasks, they appear in the all_tasks
# """
# def test_add_two_tasks_to_tasklist():
#     tasklist = TaskList()
#     task_1 = TaskList("My first task", False)
#     task_2 = TaskList("My second task", False)
#     tasklist.add_task(task_1)
#     tasklist.add_task(task_2)
#     assert tasklist.all_tasks

# """



# @TaskList
# all_tasks 
# add_tasks
# Test that when we add a task it appears in the all_tasks
# """
# def test_add_task_to_tasklist():
#     tasklist = TaskList()
#     task_1 = TaskList("My first task", False)
#     tasklist.add_task(task_1)
#     assert tasklist.all_tasks
