import json
import os
import sys

try:
    import tkinter as tk
    from tkinter import simpledialog, messagebox
except ImportError:
    tk = None
    simpledialog = None
    messagebox = None

DATA_FILE = "tasks.json"


class ToDoList:
    def __init__(self, filename=DATA_FILE):
        self.filename = filename
        self.tasks = []
        self.load()

    def load(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r", encoding="utf-8") as f:
                    self.tasks = json.load(f)
            except (ValueError, IOError):
                self.tasks = []
        else:
            self.tasks = []

    def save(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.tasks, f, indent=2, ensure_ascii=False)

    def add(self, text):
        if text:
            self.tasks.append({"text": text.strip(), "done": False})
            self.save()

    def toggle(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = not self.tasks[index]["done"]
            self.save()

    def remove(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save()

    def list_items(self):
        return [
            f"{i + 1}. [{'x' if task['done'] else ' '}] {task['text']}"
            for i, task in enumerate(self.tasks)
        ]


def cli_menu(todo):
    while True:
        print("\nTo-Do List")
        for line in todo.list_items():
            print(line)
        print("\nCommands:")
        print("  add <task>")
        print("  toggle <number>")
        print("  remove <number>")
        print("  gui")
        print("  quit")
        command = input("> ").strip()
        if not command:
            continue
        parts = command.split(maxsplit=1)
        action = parts[0].lower()
        arg = parts[1] if len(parts) > 1 else ""

        if action == "add":
            todo.add(arg)
        elif action == "toggle":
            if arg.isdigit():
                todo.toggle(int(arg) - 1)
            else:
                print("Enter a valid task number.")
        elif action == "remove":
            if arg.isdigit():
                todo.remove(int(arg) - 1)
            else:
                print("Enter a valid task number.")
        elif action == "gui":
            if tk:
                run_gui(todo)
                return
            else:
                print("Tkinter is not available.")
        elif action in ("quit", "exit"):
            return
        else:
            print("Unknown command.")


def run_gui(todo):
    root = tk.Tk()
    root.title("To-Do List")

    listbox = tk.Listbox(root, width=50, height=15)
    listbox.pack(padx=10, pady=10, fill="both", expand=True)

    def refresh():
        listbox.delete(0, tk.END)
        for item in todo.list_items():
            listbox.insert(tk.END, item)

    def add_task():
        text = simpledialog.askstring("Add Task", "Task:")
        if text:
            todo.add(text)
            refresh()

    def toggle_task():
        selection = listbox.curselection()
        if not selection:
            return
        todo.toggle(selection[0])
        refresh()

    def remove_task():
        selection = listbox.curselection()
        if not selection:
            return
        if messagebox.askyesno("Remove Task", "Remove selected task?"):
            todo.remove(selection[0])
            refresh()

    button_frame = tk.Frame(root)
    button_frame.pack(padx=10, pady=5, fill="x")

    tk.Button(button_frame, text="Add", command=add_task).pack(side="left", padx=5)
    tk.Button(button_frame, text="Toggle", command=toggle_task).pack(side="left", padx=5)
    tk.Button(button_frame, text="Remove", command=remove_task).pack(side="left", padx=5)
    tk.Button(button_frame, text="Quit", command=root.destroy).pack(side="right", padx=5)

    refresh()
    root.mainloop()


if __name__ == "__main__":
    todo = ToDoList()
    if len(sys.argv) > 1 and sys.argv[1].lower() == "gui":
        if tk:
            run_gui(todo)
        else:
            print("Tkinter is not available.")
    else:
        cli_menu(todo)