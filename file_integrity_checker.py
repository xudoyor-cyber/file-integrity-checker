import hashlib
import json
import os
from rich import print
from rich.table import Table

DB_FILE = "hashes.json"


def calculate_hash(file_path):
    """Calculate SHA-256 hash of a file."""
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(8192):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        return None


def load_db():
    """Load saved file hashes."""
    if not os.path.exists(DB_FILE):
        return {}

    with open(DB_FILE, "r") as f:
        return json.load(f)


def save_db(hashes):
    """Save file hashes."""
    with open(DB_FILE, "w") as f:
        json.dump(hashes, f, indent=4)


def add_file(file_path):
    hashes = load_db()
    file_hash = calculate_hash(file_path)

    if file_hash is None:
        print(f"[red]File not found:[/red] {file_path}")
        return

    hashes[file_path] = file_hash
    save_db(hashes)
    print(f"[green]Added file to tracking:[/green] {file_path}")


def check_integrity():
    hashes = load_db()

    if not hashes:
        print("[yellow]No files are being tracked yet.[/yellow]")
        return

    table = Table(title="File Integrity Check")
    table.add_column("File", style="cyan")
    table.add_column("Status", style="magenta")

    for file_path, old_hash in hashes.items():
        new_hash = calculate_hash(file_path)

        if new_hash is None:
            table.add_row(file_path, "[red]DELETED[/red]")
        elif new_hash != old_hash:
            table.add_row(file_path, "[red]MODIFIED[/red]")
        else:
            table.add_row(file_path, "[green]OK[/green]")

    print(table)


def menu():
    while True:
        print("\n[bold cyan]File Integrity Checker[/bold cyan]")
        print("1. Add file to tracking")
        print("2. Check integrity")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            path = input("Enter file path: ")
            add_file(path)
        elif choice == "2":
            check_integrity()
        elif choice == "3":
            print("[bold yellow]Goodbye![/bold yellow]")
            break
        else:
            print("[red]Invalid choice.[/red]")


if __name__ == "__main__":
    menu()

