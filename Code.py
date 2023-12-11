import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class TaskBudgetManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TaskBud: Task and Budget Buddy")

        # Load and resize the logo
        logo_path = "TaskBud.png"  
        logo_image = Image.open(logo_path)
        logo_image = logo_image.resize((400, 400))
        logo_photo = ImageTk.PhotoImage(logo_image)

        logo_label = tk.Label(root, image=logo_photo)
        logo_label.image = logo_photo
        logo_label.grid(row=0, column=0, columnspan=3, pady=(10, 0))

        # Notebook to switch between Task and Budget tabs
        notebook = ttk.Notebook(root)
        notebook.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Task Management tab
        task_frame = ttk.Frame(notebook)
        notebook.add(task_frame, text="Task Management")
        self.setup_task_frame(task_frame)

        # Budget Management tab
        budget_frame = ttk.Frame(notebook)
        notebook.add(budget_frame, text="Budget Management")
        self.setup_budget_frame(budget_frame)

    def setup_task_frame(self, frame):
        tk.Label(frame, text="Task Management", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=3, pady=(10, 20))

        tasks = []

        def add_task():
            task_name = task_name_entry.get()
            deadline = deadline_entry.get()

            task = {"name": task_name, "deadline": deadline}
            tasks.append(task)

            result_label.config(text=f"Task '{task_name}' added successfully!")

        def view_tasks():
            if not tasks:
                result_label.config(text="No tasks to display.")
            else:
                sorted_tasks = self.quicksort(tasks)
                result_label.config(text="Tasks sorted by deadline:")
                for idx, task in enumerate(sorted_tasks, start=1):
                    result_label.config(text=f"{idx}. {task['name']} - Deadline: {task['deadline']}")

        tk.Label(frame, text="Task Name:").grid(row=1, column=0, pady=(0, 5))
        task_name_entry = tk.Entry(frame)
        task_name_entry.grid(row=1, column=1, pady=(0, 5))

        tk.Label(frame, text="Deadline (YYYY-MM-DD):").grid(row=2, column=0, pady=(0, 5))
        deadline_entry = tk.Entry(frame)
        deadline_entry.grid(row=2, column=1, pady=(0, 5))

        add_button = tk.Button(frame, text="Add Task", command=add_task)
        add_button.grid(row=3, column=0, pady=(10, 0))

        view_button = tk.Button(frame, text="View Tasks", command=view_tasks)
        view_button.grid(row=3, column=1, pady=(10, 0))

        result_label = tk.Label(frame, text="")
        result_label.grid(row=4, column=0, columnspan=2, pady=(10, 0))

    def setup_budget_frame(self, frame):
        tk.Label(frame, text="Budget Management", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=3, pady=(10, 20))

        budget = tk.StringVar()
        expenses = []

        def add_expense():
            expense_name = expense_name_entry.get()
            expense_amount = expense_amount_entry.get()

            expense = {"name": expense_name, "amount": float(expense_amount)}
            expenses.append(expense)

            result_label.config(text=f"Expense '{expense_name}' added successfully!")

        def view_expenses():
            if not expenses:
                result_label.config(text="No expenses to display.")
            else:
                total_expenses = sum(expense['amount'] for expense in expenses)
                result_label.config(text="Expenses:")
                for idx, expense in enumerate(expenses, start=1):
                    result_label.config(text=f"{idx}. {expense['name']} - Amount: {expense['amount']}")

                result_label.config(text=f"\nTotal Expenses: {total_expenses}")
                remaining_budget = float(budget.get()) - total_expenses
                result_label.config(text=f"Remaining Budget: {remaining_budget}")

        tk.Label(frame, text="Monthly Budget:").grid(row=1, column=0, pady=(0, 5))
        budget_entry = tk.Entry(frame, textvariable=budget)
        budget_entry.grid(row=1, column=1, pady=(0, 5))

        tk.Label(frame, text="Expense Name:").grid(row=2, column=0, pady=(0, 5))
        expense_name_entry = tk.Entry(frame)
        expense_name_entry.grid(row=2, column=1, pady=(0, 5))

        tk.Label(frame, text="Expense Amount:").grid(row=3, column=0, pady=(0, 5))
        expense_amount_entry = tk.Entry(frame)
        expense_amount_entry.grid(row=3, column=1, pady=(0, 5))

        add_button = tk.Button(frame, text="Add Expense", command=add_expense)
        add_button.grid(row=4, column=0, pady=(10, 0))

        view_button = tk.Button(frame, text="View Expenses", command=view_expenses)
        view_button.grid(row=4, column=1, pady=(10, 0))

        result_label = tk.Label(frame, text="")
        result_label.grid(row=5, column=0, columnspan=2, pady=(10, 0))

    def quicksort(self, tasks):
        if len(tasks) <= 1:
            return tasks
        else:
            pivot = tasks.pop()

            less_than_pivot = []
            greater_than_pivot = []

            for task in tasks:
                if task['deadline'] < pivot['deadline']:
                    less_than_pivot.append(task)
                else:
                    greater_than_pivot.append(task)

            return self.quicksort(less_than_pivot) + [pivot] + self.quicksort(greater_than_pivot)

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskBudgetManagerApp(root)
    root.mainloop()
