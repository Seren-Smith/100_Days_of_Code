import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os
from datetime import datetime

class ProductivityTrackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Productivity Tracker")
        self.root.geometry("500x400")

        # Data management
        self.data_file = "productivity_data.json"
        self.user_data = {}
        self.current_tasks = []
        self.current_user = ""
        self.load_data()

        # Create all widgets
        self.create_widgets()
        self.show_login_screen()

    def load_data(self):
        """Load existing user data from file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    self.user_data = json.load(f)
            except:
                self.user_data = {}

    def save_data(self):
        """Save user data to file"""
        with open(self.data_file, 'w') as f:
            json.dump(self.user_data, f, indent=4)

    def create_widgets(self):
        """Create all GUI widgets"""
        # Login Frame
        self.login_frame = tk.Frame(self.root)
        self.name_label = tk.Label(self.login_frame, text="Enter Your Name:")
        self.name_entry = tk.Entry(self.login_frame, width=30)
        self.login_button = tk.Button(self.login_frame, text="Start Tracking",
                                      command=self.handle_login, bg="#4CAF50", fg="white")

        # Main Application Frame
        self.main_frame = tk.Frame(self.root)

        # Task List
        self.task_listbox = tk.Listbox(self.main_frame, height=15, width=50,
                                       selectbackground="#a6a6a6", selectmode=tk.SINGLE)
        self.scrollbar = tk.Scrollbar(self.main_frame, orient=tk.VERTICAL)
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        # Buttons
        button_frame = tk.Frame(self.main_frame)
        self.add_button = tk.Button(button_frame, text="Add Task",
                                    command=self.add_task, bg="#2196F3", fg="white")
        self.toggle_button = tk.Button(button_frame, text="Toggle Complete",
                                       command=self.toggle_task, bg="#FF9800", fg="white")
        self.stats_button = tk.Button(button_frame, text="View Stats",
                                      command=self.show_stats, bg="#607D8B", fg="white")
        self.save_button = tk.Button(button_frame, text="Save & Exit",
                                     command=self.save_and_exit, bg="#F44336", fg="white")

        # Layout
        self.name_label.pack(pady=5)
        self.name_entry.pack(pady=5)
        self.login_button.pack(pady=10)

        self.task_listbox.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.scrollbar.grid(row=0, column=1, sticky="ns", pady=5)

        button_frame.grid(row=1, column=0, columnspan=2, pady=10)
        self.add_button.pack(side=tk.LEFT, padx=5, ipadx=5)
        self.toggle_button.pack(side=tk.LEFT, padx=5, ipadx=5)
        self.stats_button.pack(side=tk.LEFT, padx=5, ipadx=5)
        self.save_button.pack(side=tk.LEFT, padx=5, ipadx=5)

        # Configure grid weights
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

    def show_login_screen(self):
        """Show the login screen"""
        self.main_frame.grid_forget()
        self.login_frame.pack(pady=50)
        self.name_entry.focus()

    def show_main_screen(self):
        """Show the main application screen"""
        self.login_frame.pack_forget()
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    def handle_login(self):
        """Handle user login"""
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showerror("Error", "Please enter your name")
            return

        self.current_user = name.title()  # Capitalize name properly
        today = str(datetime.now().date())

        # Initialize user if new
        if self.current_user not in self.user_data:
            self.user_data[self.current_user] = {
                'join_date': today,
                'task_history': {},
                'categories': {}
            }

        # Load today's tasks or create new
        if today in self.user_data[self.current_user]['task_history']:
            self.current_tasks = self.user_data[self.current_user]['task_history'][today]
        else:
            self.current_tasks = []

        self.update_task_list()
        self.show_main_screen()

    def update_task_list(self):
        """Update the listbox with current tasks"""
        self.task_listbox.delete(0, tk.END)

        for i, task in enumerate(self.current_tasks, 1):
            status = "✓" if task['completed'] else " "
            display_text = f"{i}. [{status}] {task['name']}"
            self.task_listbox.insert(tk.END, display_text)

            # Color completed tasks differently
            if task['completed']:
                self.task_listbox.itemconfig(tk.END, {'fg': 'gray'})

    def add_task(self):
        """Add a new task"""
        task_name = simpledialog.askstring("Add Task", "Enter task description:")
        if task_name and task_name.strip():
            self.current_tasks.append({
                'name': task_name.strip(),
                'completed': False,
                'added': str(datetime.now())
            })
            self.update_task_list()

    def toggle_task(self):
        """Toggle task completion status"""
        selection = self.task_listbox.curselection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a task first")
            return

        index = selection[0]
        self.current_tasks[index]['completed'] = not self.current_tasks[index]['completed']
        self.current_tasks[index]['completed_at'] = str(datetime.now()) if self.current_tasks[index][
            'completed'] else None
        self.update_task_list()

    def show_stats(self):
        """Show productivity statistics"""
        total = len(self.current_tasks)
        completed = sum(1 for task in self.current_tasks if task['completed'])
        pct = (completed / total * 100) if total > 0 else 0

        stats = (
            f"Productivity Stats for {self.current_user}\n\n"
            f"Tasks: {completed}/{total} completed\n"
            f"Completion: {pct:.1f}%\n\n"
        )

        if total > 0:
            if pct == 0:
                stats += "Let's get started! You haven't completed any tasks yet."
            elif pct < 50:
                stats += "Good start! Keep going!"
            elif pct < 100:
                stats += "Great progress! You're almost there!"
            else:
                stats += "Amazing! All tasks completed!"

        messagebox.showinfo("Productivity Stats", stats)

    def save_and_exit(self):
        """Save current session and exit"""
        today = str(datetime.now().date())
        if self.current_user:  # Only save if we have a logged in user
            self.user_data[self.current_user]['task_history'][today] = self.current_tasks
            self.save_data()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = ProductivityTrackerGUI(root)
    root.mainloop()
