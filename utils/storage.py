import os
import json

DATA_FILE = os.path.join(os.path.dirname(__file__), "../data/data.json")

def load_data() -> dict:
    """Loads application state data from a JSON file."""
    if not os.path.exists(DATA_FILE):
        # Default structured empty schema
        return {"users": {}, "projects": {}, "tasks": {}}
    
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, TypeError):
        print("[Warning] Data file corrupted. Starting with an empty database.")
        return {"users": {}, "projects": {}, "tasks": {}}

def save_data(data: dict) -> None:
    """Saves application state data to a JSON file."""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)
    except IOError as e:
        print(f"[Error] Failed to write data to disk: {e}")