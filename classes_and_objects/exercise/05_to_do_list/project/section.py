from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks: list[Task] = []

    def add_task(self, task: Task) -> str:
        if task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(task)
        return f"Task {task.details()} is added to the section"

    def complete_task(self, task_name: str) ->str:
        task_str = next((task_str for task_str in self.tasks if task_str.name == task_name), None)
        if task_str:
            task_str.completed = True
            return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self) -> str:
        len_tasks = len(self.tasks)
        self.tasks = [t for t in self.tasks if not t.completed]
        return f"Cleared {len_tasks - len(self.tasks)} tasks."

    def view_section(self) -> str:
        result = [f"Section {self.name}:"]
        for task in self.tasks:
            result.append(task.details())

        return "\n".join(result)