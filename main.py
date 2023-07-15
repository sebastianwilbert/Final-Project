import tkinter
from tkinter import*
root=Tk()
root.title("ToDoList")
root.geometry("400x650")
root.resizable(True,True)
root.configure(bg="lightblue")
todo_list = []



icon=PhotoImage(file="1950715.png")

root.iconphoto(False,icon)

heading=Label(root,text="To Do", font="msserif 30 bold", fg="lightpink", bg="lightblue")

heading.place(x=145, y=30)

def display_list():
    if len(todo_list) == 0:
        print("No items in the to-do list.")
    else:
        print("To-Do List:")
        for i, item in enumerate(todo_list, 1):
            print(f"{i}. {item}")

frame=Frame(root, width=400, height=50, bg="lightpink")
frame.place(x=0, y=180)

start=Entry(frame, width=20, font="msserif 20 bold", bd=0)
start.place(x=94,y=7)
start.focus()

button=Button(frame,text="+", font="msserif 20 bold", width=5, bg="#C0AFE2", fg="white", bd=0)
button.place(x=0, y=0)

box=Frame(root, bd=1, width=700, height=280, bg="lightblue")
box.pack(pady=(260, 0))
list=Listbox(box, font="msserif 20 bold", width=25, height=11, bg="lightpink", cursor="hand2")
list.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar=Scrollbar(box)
scrollbar.pack(side= RIGHT, fill=BOTH)

list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=list.yview)
root.mainloop()


