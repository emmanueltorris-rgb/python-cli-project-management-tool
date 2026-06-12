# Project Management CLI Tool

A command-line interface for managing users, projects, and tasks with local JSON storage.

## Project Structure

```
project_cli/
├── data/
│   └── data.json           # Local storage for users, projects, and tasks
├── models/
│   ├── __init__.py
│   ├── person.py           # Base class (Inheritance)
│   ├── user.py             # User model
│   ├── project.py          # Project model
│   └── task.py             # Task model
├── utils/
│   ├── __init__.py
│   └── storage.py          # JSON serialization & File I/O helpers
├── main.py                 # CLI entry point using argparse
├── requirements.txt        # External dependencies (rich)
└── README.md               # Setup and usage guide
```

## Setup

### Prerequisites
- Python 3.7+

### Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Users

List all users:
```bash
python main.py user list
```

Add a new user:
```bash
python main.py user add
```

### Projects

List all projects:
```bash
python main.py project list
```

Add a new project:
```bash
python main.py project add
```

### Tasks

List all tasks:
```bash
python main.py task list
```

Add a new task:
```bash
python main.py task add
```

## Features

- **Inheritance**: `User` class extends `Person` base class
- **JSON Storage**: Local data persistence with automatic file I/O
- **CLI Interface**: Using argparse for command-line argument parsing
- **Rich Output**: Support for formatted console output (ready to integrate)

## Models

### Person (Base Class)
- `name`: Person's name
- `email`: Person's email address

### User (extends Person)
- `user_id`: Unique identifier
- `name`: User's name
- `email`: User's email address

### Project
- `project_id`: Unique identifier
- `name`: Project name
- `description`: Project description
- `owner_id`: ID of the project owner
- `tasks`: List of associated tasks

### Task
- `task_id`: Unique identifier
- `title`: Task title
- `description`: Task description
- `project_id`: Associated project ID
- `assigned_to`: User ID of assignee
- `status`: Task status (pending, in_progress, completed)


# python-cli-project-management-tool
