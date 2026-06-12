from utils.storage import load_data, save_data

class Project:
    """Project entity representing a body of work assigned to a User."""
    def __init__(self, title: str, user: str, description: str, due_date: str):
        self.title = title
        self.user = user
        self.description = description
        self.due_date = due_date

    @classmethod
    def create(cls, title: str, user: str, description: str, due_date: str):
        """Creates and links a project to an existing user."""
        data = load_data()
        if user not in data["users"]:
            raise ValueError(f"User '{user}' does not exist. Create the user first.")
        if title in data["projects"]:
            raise ValueError(f"Project '{title}' already exists.")
            
        data["projects"][title] = {
            "user": user,
            "description": description,
            "due_date": due_date
        }
        save_data(data)
        return cls(title, user, description, due_date)

    @classmethod
    def get_all(cls) -> list:
        """Retrieves all registered projects."""
        data = load_data()
        return [cls(title, info["user"], info["description"], info["due_date"]) 
                for title, info in data["projects"].items()]

    def __repr__(self) -> str:
        return f"Project('{self.title}', Owner: {self.user}, Due: {self.due_date})"