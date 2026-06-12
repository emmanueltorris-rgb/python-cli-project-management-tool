from utils.storage import load_data, save_data

class Task:
    """Task entity representing discrete milestones mapped within a project."""
    def __init__(self, title: str, project: str, assigned_to: str, status: str = "Pending"):
        self.title = title
        self.project = project
        self.assigned_to = assigned_to
        self.status = status

    @classmethod
    def create(cls, title: str, project: str, assigned_to: str):
        """Creates a new task linked to a target project."""
        data = load_data()
        if project not in data["projects"]:
            raise ValueError(f"Project '{project}' does not exist.")
        if assigned_to not in data["users"]:
            raise ValueError(f"Assignee User '{assigned_to}' does not exist.")
        
        task_id = f"{project}::{title}"
        if task_id in data["tasks"]:
            raise ValueError(f"Task '{title}' already exists within project '{project}'.")

        data["tasks"][task_id] = {
            "title": title,
            "project": project,
            "assigned_to": assigned_to,
            "status": "Pending"
        }
        save_data(data)
        return cls(title, project, assigned_to)

    @classmethod
    def complete(cls, project: str, title: str):
        """Marks an existing task status as Completed."""
        data = load_data()
        task_id = f"{project}::{title}"
        if task_id not in data["tasks"]:
            raise ValueError(f"Task '{title}' under Project '{project}' not found.")
        
        data["tasks"][task_id]["status"] = "Completed"
        save_data(data)

    @classmethod
    def get_all(cls) -> list:
        """Retrieves all tasks across all projects."""
        data = load_data()
        return [cls(info["title"], info["project"], info["assigned_to"], info["status"]) 
                for info in data["tasks"].values()]