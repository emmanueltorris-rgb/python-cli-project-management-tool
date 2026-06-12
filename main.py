import argparse
from models.user import User
from models.project import Project
from models.task import Task
from rich.console import Console
from rich.table import Table

console = Console()

def handle_add_user(args):
    try:
        user = User.create(name=args.name, email=args.email)
        console.print(f"[bold green]✔ User '{user.name}' successfully added![/bold green]")
    except ValueError as e:
        console.print(f"[bold red]Error:[/bold red] {e}")

def handle_add_project(args):
    try:
        project = Project.create(title=args.title, user=args.user, description=args.desc, due_date=args.due)
        console.print(f"[bold green]✔ Project '{project.title}' assigned to {project.user}![/bold green]")
    except ValueError as e:
        console.print(f"[bold red]Error:[/bold red] {e}")

def handle_add_task(args):
    try:
        task = Task.create(title=args.title, project=args.project, assigned_to=args.assigned_to)
        console.print(f"[bold green]✔ Task '{task.title}' bound to Project '{task.project}' successfully.[/bold green]")
    except ValueError as e:
        console.print(f"[bold red]Error:[/bold red] {e}")

def handle_complete_task(args):
    try:
        Task.complete(project=args.project, title=args.title)
        console.print(f"[bold blue]✔ Task '{args.title}' marked as COMPLETED.[/bold blue]")
    except ValueError as e:
        console.print(f"[bold red]Error:[/bold red] {e}")

def handle_list_dashboard(args):
    # Fetch lists from database
    users = User.get_all()
    projects = Project.get_all()
    tasks = Task.get_all()

    # Create Rich Tables for CLI output visualization
    console.print("\n[bold magenta]=== SYSTEM DASHBOARD ===[/bold magenta]\n")
    
    # Projects Table
    proj_table = Table(title="Projects Database", show_header=True, header_style="bold cyan")
    proj_table.add_column("Project Title", style="yellow")
    proj_table.add_column("Owner (User)")
    proj_table.add_column("Due Date")
    for p in projects:
        proj_table.add_row(p.title, p.user, p.due_date)
    console.print(proj_table)

    # Tasks Table
    task_table = Table(title="Tasks Progress Ledger", show_header=True, header_style="bold green")
    task_table.add_column("Task Title", style="yellow")
    task_table.add_column("Associated Project")
    task_table.add_column("Assignee")
    task_table.add_column("Status")
    for t in tasks:
        status_style = "[green]Completed[/green]" if t.status == "Completed" else "[red]Pending[/red]"
        task_table.add_row(t.title, t.project, t.assigned_to, status_style)
    console.print(task_table)

def main():
    parser = argparse.ArgumentParser(description="Multi-User Project Management CLI Engine")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # add-user subcommand
    p_add_user = subparsers.add_parser("add-user", help="Register a new system user")
    p_add_user.add_argument("--name", required=True, help="Unique string identifier name")
    p_add_user.add_argument("--email", required=True, help="User email address")
    p_add_user.set_defaults(func=handle_add_user)

    # add-project subcommand
    p_add_proj = subparsers.add_parser("add-project", help="Create a brand new project scope")
    p_add_proj.add_argument("--title", required=True, help="Project name identifier")
    p_add_proj.add_argument("--user", required=True, help="Owner user account name")
    p_add_proj.add_argument("--desc", default="No description provided", help="Brief notes")
    p_add_proj.add_argument("--due", default="TBD", help="Project finalization date target")
    p_add_proj.set_defaults(func=handle_add_project)

    # add-task subcommand
    p_add_task = subparsers.add_parser("add-task", help="Appends execution tasks to active projects")
    p_add_task.add_argument("--title", required=True, help="Task headline description")
    p_add_task.add_argument("--project", required=True, help="Target project environment")
    p_add_task.add_argument("--assigned-to", required=True, help="User tasked with running this item")
    p_add_task.set_defaults(func=handle_add_task)

    # complete-task subcommand
    p_comp_task = subparsers.add_parser("complete-task", help="Resolve and close an open project task item")
    p_comp_task.add_argument("--project", required=True, help="Parent project name context")
    p_comp_task.add_argument("--title", required=True, help="The exact task name to resolve")
    p_comp_task.set_defaults(func=handle_complete_task)

    # list-dashboard subcommand
    p_list = subparsers.add_parser("list-dashboard", help="Print overall status matrix tables")
    p_list.set_defaults(func=handle_list_dashboard)

    # Route Action execution
    args = parser.parse_parse = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()