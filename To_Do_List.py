import tkinter as tk
from tkinter import messagebox, simpledialog

# make window
root = tk.Tk()
root.title("Colorful To-Do List App")
root.geometry("450x550")
root.resizable(False, False)

# Global task list
tasks = []

# Task list update function
def update_listbox():
    listbox.delete(0, tk.END)
    for idx, (task, status) in enumerate(tasks):
        display_task = f"{idx+1}. {task}"
        listbox.insert(tk.END, display_task)
        if status:
            listbox.itemconfig(idx, {'fg': 'green'})  # Completed task green color
        else:
            listbox.itemconfig(idx, {'fg': 'black'})  # Normal task black color

# Task Add Function
def add_task():
    task = entry.get()
    if task:
        tasks.append((task, False))
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Task update function
def update_task():
    try:
        selected_index = listbox.curselection()[0]
        current_task, status = tasks[selected_index]
        new_task = simpledialog.askstring("Update Task", "Edit your task:", initialvalue=current_task)
        if new_task:
            tasks[selected_index] = (new_task, status)
            update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update.")

# Task Done Function
def complete_task():
    try:
        selected_index = listbox.curselection()[0]
        task, _ = tasks[selected_index]
        tasks[selected_index] = (task, True)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as complete.")

# Task Delete Function
def delete_task():
    try:
        selected_index = listbox.curselection()[0]
        tasks.pop(selected_index)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# --- UI Elements ---

# Title level
label = tk.Label(root, text="Colorful To-Do List", font=("Helvetica", 20, "bold"))
label.pack(pady=10)

# Entry field
entry = tk.Entry(root, font=("Helvetica", 14))
entry.pack(pady=10, padx=20, fill=tk.X)

# Button frame
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Buttons
add_btn = tk.Button(button_frame, text="Add Task", width=12, command=add_task)
add_btn.grid(row=0, column=0, padx=5)

update_btn = tk.Button(button_frame, text="Update Task", width=12, command=update_task)
update_btn.grid(row=0, column=1, padx=5)

complete_btn = tk.Button(button_frame, text="Mark as Done", width=12, command=complete_task)
complete_btn.grid(row=0, column=2, padx=5)

delete_btn = tk.Button(button_frame, text="Delete Task", width=12, command=delete_task)
delete_btn.grid(row=1, column=1, pady=10)

# ListBox
listbox = tk.Listbox(root, font=("Helvetica", 14), width=50, height=20)
listbox.pack(pady=10)

# Running the window
root.mainloop()
