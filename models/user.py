from models.person import Person
from utils.storage import load_data, save_data

class User(Person):
    """User entity containing an email and associated project lookups."""
    def __init__(self, name: str, email: str):
        super().__init__(name)
        self.email = email

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str):
        if "@" not in value or "." not in value:
            raise ValueError("Invalid email format.")
        self._email = value

    @classmethod
    def create(cls, name: str, email: str):
        """Class method to store and instantiate a new User."""
        data = load_data()
        if name in data["users"]:
            raise ValueError(f"User '{name}' already exists.")
        
        data["users"][name] = {"email": email}
        save_data(data)
        return cls(name, email)

    @classmethod
    def get_all(cls) -> list:
        """Retrieves all users from data storage."""
        data = load_data()
        return [cls(name, details["email"]) for name, details in data["users"].items()]

    def __repr__(self) -> str:
        return f"User(Name: {self.name}, Email: {self.email})"