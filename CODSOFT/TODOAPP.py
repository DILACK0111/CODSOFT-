import tkinter as tk

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except IndexError:
        pass

def update_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        updated_task = entry_task.get()
        listbox_tasks.delete(task_index)
        listbox_tasks.insert(task_index, updated_task)
        entry_task.delete(0, tk.END)
    except IndexError:
        pass

def track_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        task_status = "Completed" if task_index in completed_tasks else "Pending"
        label_status.config(text=f"Task Status: {task_status}")
    except IndexError:
        pass

def archive_task():
    global completed_tasks
    try:
        task_index = listbox_tasks.curselection()[0]
        completed_tasks.add(task_index)
        listbox_tasks.itemconfig(task_index, {'bg': 'lightgrey'})
    except IndexError:
        pass

# Initialize the main window
root = tk.Tk()
root.title("To-Do App")

# Task Entry
frame_input = tk.Frame(root)
frame_input.pack(padx=10, pady=5, fill=tk.BOTH)

entry_task = tk.Entry(frame_input, width=40)
entry_task.pack(side=tk.LEFT, padx=5)

button_add = tk.Button(frame_input, text="Add Task", width=10, command=add_task)
button_add.pack(side=tk.LEFT, padx=5)

button_update = tk.Button(frame_input, text="Update Task", width=10, command=update_task)
button_update.pack(side=tk.LEFT, padx=5)

# Task List
frame_tasks = tk.Frame(root)
frame_tasks.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

listbox_tasks = tk.Listbox(frame_tasks, width=50, height=15)
listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

# Task Status
frame_status = tk.Frame(root)
frame_status.pack(padx=10, pady=5, fill=tk.BOTH)

label_status = tk.Label(frame_status, text="Task Status: ")
label_status.pack()

button_track = tk.Button(frame_status, text="Track Task", width=10, command=track_task)
button_track.pack(side=tk.LEFT, padx=5)

button_archive = tk.Button(frame_status, text="Archive Task", width=12, command=archive_task)
button_archive.pack(side=tk.LEFT, padx=5)

# Set up completed tasks set
completed_tasks = set()

root.mainloop()
