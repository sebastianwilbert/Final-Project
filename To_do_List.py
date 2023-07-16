import tkinter as tk
from PIL import ImageTk, Image

task = ""
all_task = []

# Read/Create txt File
try:
    with open("TDL_Tasks") as tf:
        all_task = eval(tf.read())
except:
    open("TDL_Tasks", "w").close()


# Add Array to txt File
def file_add_task(*args):
    open("TDL_Tasks", "w").close()
    task_file = open("TDL_Tasks", "r+")
    task_file.write(str(all_task))
    task_file.close()


# Add Task to List
def add_task(*args):
    global task
    global all_task
    task = task_input.get()
    all_task.append(task)
    task_list.insert("end", " " + task)
    task_input.delete(0, "end")
    file_add_task()


# Tick Completed Task
def update_task(*args):
    global task
    global all_task
    for i in task_list.curselection():
        task = all_task[i] + " ✔"
        all_task.pop(i)
        all_task.insert(i, task)
        task_list.delete(i)
        task_list.insert(i, " " + task)
    file_add_task()


# Delete Single Task
def delete_task(*args):
    global all_task
    for i in task_list.curselection():
        task_list.delete(i)
        all_task.pop(i)
    file_add_task()


# Clear All Task
def clear_task(*args):
    global all_task
    task_list.delete(0, "end")
    all_task.clear()
    file_add_task()


# Window
root = tk.Tk()
root.title("To-Do-List")
root.configure(bg="#A2D2FF")
root.resizable(False, False)

# Exit Hint Display
exit_text = tk.Label(root, text="Press 'Esc' to exit", bg="#A2D2FF", fg="#545454", highlightthickness=0,
                     font=("Arial", 10))
exit_text.grid(row=4, column=0, pady=5)

# Exit Key Bind
root.bind("<Escape>", lambda x: root.destroy())

# Icon
icon = ImageTk.PhotoImage(Image.open("TDL_Icon.png"))
root.iconphoto(False, icon)

# Title
heading = tk.Label(root, text="To-Do", bg="#A2D2FF", fg="#000000", font=("MS Serif", 15))
heading.grid(row=0, column=0, padx=10, pady=10)

# Frames
first_frame = tk.Frame(root, bg="#A2D2FF")
first_frame.grid(row=1, column=0, padx=10, pady=10)
second_frame = tk.Frame(root, bg="#A2D2FF")
second_frame.grid(row=2, column=0, padx=10, pady=10)
third_frame = tk.Frame(root, bg="#A2D2FF")
third_frame.grid(row=3, column=0, padx=10, pady=5)

# Input
task_input = tk.Entry(first_frame, width=20, highlightthickness=0, relief="ridge", font=("MS Serif", 15))
task_input.grid(row=0, column=1, padx=5)
add_button = tk.Button(first_frame, text="+", width=5, command=add_task, bg="#C0AFE2", fg="#000000",
                       font=("MS Serif", 15))
add_button.grid(row=0, column=0, padx=5)

# Display Task
task_list = tk.Listbox(second_frame, height=10, width=30, borderwidth=0, bg="#CDB4DB", font=("MS Serif", 15))
task_list.grid(row=3, column=0)
scrollbar = tk.Scrollbar(second_frame, orient="vertical")
scrollbar.grid(row=3, column=1, sticky="ns")
task_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_list.yview)

# Buttons
update_button = tk.Button(third_frame, text="Tick", width=5, command=update_task, bg="#FFAFCC", fg="#000000",
                          font=("MS Serif", 15))
update_button.grid(row=0, column=0, padx=10)
clear_button = tk.Button(third_frame, text="Clear", width=5, command=clear_task, bg="#FFAFCC", fg="#000000",
                         font=("MS Serif", 15))
clear_button.grid(row=0, column=1, padx=10)
delete_button = tk.Button(third_frame, text="Delete", width=5, command=delete_task, bg="#FFAFCC", fg="#000000",
                          font=("MS Serif", 15))
delete_button.grid(row=0, column=2, padx=10)

# Display Task from txt
for j in range(len(all_task)):
    task_list.insert("end", " " + all_task[j])

# Run
root.mainloop()
