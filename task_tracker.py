def task_tracker():
    get_task = input("What task do you want to track? ")
    return get_task


tasks = []

for number in range(3):
    task = task_tracker()
    tasks.append(task)

print(tasks)
