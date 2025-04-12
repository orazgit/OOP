class Task:
    def __init__(self, title: str, xp: int):
        self.title = title
        self.xp = xp
        self.completed = False

    def complete(self):
        if not self.completed:
            self.completed = True
            print(f"Task '{self.title}' completed!")
        else:
            print(f"Task '{self.title}' was already completed.")

    def get_xp(self) -> int:
        return self.xp if self.completed else 0

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "xp": self.xp,
            "completed": self.completed
        }

    @staticmethod
    def from_dict(data: dict) -> 'Task':
        task = Task(data["title"], data["xp"])
        task.completed = data.get("completed", False)
        return task
