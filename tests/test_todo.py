"""Regression tests for ToDoList task input and persistence."""

import tempfile
import unittest
from pathlib import Path

from ToDoList import ToDoList


class ToDoListTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.addCleanup(self.tempdir.cleanup)
        self.path = Path(self.tempdir.name) / "tasks.json"
        self.todo = ToDoList(self.path)

    def test_whitespace_only_task_is_ignored(self):
        self.todo.add(" \t\n ")
        self.assertEqual(self.todo.tasks, [])
        self.assertFalse(self.path.exists())

    def test_empty_and_non_string_inputs_are_ignored(self):
        for value in ("", None, 42):
            self.todo.add(value)
        self.assertEqual(self.todo.tasks, [])
        self.assertFalse(self.path.exists())

    def test_valid_task_is_trimmed_and_persisted(self):
        self.todo.add("  Buy milk  ")
        self.assertEqual(self.todo.tasks, [{"text": "Buy milk", "done": False}])
        self.assertEqual(ToDoList(self.path).tasks, self.todo.tasks)

    def test_toggle_and_remove_still_persist(self):
        self.todo.add("Task")
        self.todo.toggle(0)
        self.assertEqual(ToDoList(self.path).tasks[0]["done"], True)
        self.todo.remove(0)
        self.assertEqual(ToDoList(self.path).tasks, [])


if __name__ == "__main__":
    unittest.main()
