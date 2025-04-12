from typing import List, Optional
from task import Task
from uuid import uuid4

class User:
    def __init__(
        self,
        username: str,
        email: str,
        password: str,
        xp: int = 0,
        level: int = 0,
        tasks: Optional[List[Task]] = None
    ):
        self.id: str = str(uuid4())
        self.username: str = username
        self.email: str = email
        self.password: str = password
        self.xp: int = xp
        self.level: int = level
        self.tasks: List[Task] = tasks if tasks else []
    
    def add_task(self, task: Task):
        pass
    def complete_task(self, task_id: str):
        pass #check task with for loop
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "xp": self.xp,
            "level": self.level,
            "tasks": [task.to_dict() for task in self.tasks]
        }
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            username=data["username"],
            email=data["email"],
            password=data["password"],
            xp=data.get("xp", 0),
            level=data.get("level", 1)
    )
