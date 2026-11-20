# Python Task Tracker

A command-line task tracker built while learning Python functions, lists, and loops.

## What it does

- Asks for three tasks.
- Adds each task to a list.
- Prints the complete list.

Tasks are held in memory for the current run. This version does not save tasks to a file.

## Run

Install Python 3, download or clone this repository, then run from the project folder:

```sh
python task_tracker.py
```

On systems where Python 3 uses the `python3` command:

```sh
python3 task_tracker.py
```

No additional packages are required.

## Example

```text
What task do you want to track? Study Python
What task do you want to track? Go fishing
What task do you want to track? Eat
['Study Python', 'Go fishing', 'Eat']
```

## Concepts practiced

- Defining and calling a function
- Collecting text with `input()`
- Returning a value and assigning it to a variable
- Creating a list and using `.append()`
- Repeating work with `for` and `range()`
- Using indentation to organize code blocks

## Next steps

- Display each task on its own line.
- Let the user choose when to stop adding tasks.
- Mark tasks complete.
- Save and load tasks between runs.
