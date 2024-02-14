import tkinter 
from tkinter import *
from datetime import datetime

root=Tk()
root.title("To-Do-List")
root.geometry("400x650+400+100")
root.resizable(False,False)

task_list=[]
complete_count = 0
status_label = None  # Define status_label globally
last_date = None

def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)
    
    if task:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        task_with_time = f"{current_time} - {task} - Pending"
        
        with open("Screenshots/tasklist.txt.txt", 'a') as taskfile:
            taskfile.write(f"\n{task_with_time}")
            
        task_list.append(task_with_time)
        listbox.insert(END, task_with_time)

        updateStatus()

def deleteTask():
    global task_list, complete_count
    task = str(listbox.get(ANCHOR))

    if task in task_list:    
        if "Complete" in task:
            complete_count -= 1
        task_list.remove(task)
        
        with open("Screenshots/tasklist.txt.txt", 'w') as taskfile:
            for task in task_list:
                taskfile.write(task + "\n")
                
        listbox.delete(ANCHOR)

        updateStatus()

def markComplete():
    global complete_count
    selected_index = listbox.curselection()
    
    if selected_index:
        task_index = selected_index[0]
        task = listbox.get(task_index)
        
        if "Pending" in task:
            updated_task = task.replace("Pending", "Complete")
            listbox.delete(task_index)
            listbox.insert(task_index, updated_task)
            complete_count += 1

            # Update status label
            updateStatus()

            # Update task list in the file
            task_list[task_index] = updated_task
            with open("Screenshots/tasklist.txt.txt", 'w') as taskfile:
                for task in task_list:
                    taskfile.write(task + "\n")

def updateStatus():
    global status_label
    status_label.config(text=f"Complete: {complete_count} / Pending: {len(task_list)-complete_count}")

def openTaskFile():
    global status_label, last_date
    try:
        global task_list, complete_count
        with open("Screenshots/tasklist.txt.txt", "r") as taskfile:
            tasks = taskfile.readlines()
            
        for task in tasks:
            if task.strip() != "":
                task_list.append(task)
                listbox.insert(END, task)
                if "Complete" in task:
                    complete_count += 1

        status_label = Label(root, text=f"Complete: {complete_count} / Pending: {len(task_list)-complete_count}", font="arial 12", fg="black")
        status_label.place(x=10, y=630)  # Adjusted position of the status label

        # Check if it's a new day
        current_date = datetime.now().strftime("%Y-%m-%d")
        if current_date != last_date:
            last_date = current_date
            # Clear task list and update file
            task_list.clear()
            with open("Screenshots/tasklist.txt.txt", 'w') as taskfile:
                taskfile.write("")
            # Update status label
            updateStatus()

    except FileNotFoundError:
        with open("Screenshots/tasklist.txt.txt", 'w'):
            pass

def showCompletedList():
    completed_window = Toplevel(root)
    completed_window.title("Completed Tasks")
    completed_window.geometry("300x300")
    
    completed_label = Label(completed_window, text="Completed Tasks", font="arial 16 bold")
    completed_label.pack()

    completed_tasks = [task for task in task_list if "Complete" in task]
    for task in completed_tasks:
        task_label = Label(completed_window, text=task, font="arial 12")
        task_label.pack()

heading = Label(root, text="All TASK", font="arial 20 bold", fg="#5AAB70")
heading.place(x=130, y=20)

frame = Frame(root, width=400, height=50, bg="white")
frame.place(x=0, y=100)

task = StringVar()
task_entry = Entry(frame, width=18, font="arial 20", bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()

button = Button(text="Add", font="arial 20 bold", width=6, bg="#CBD18F", fg="#3A6B35", bd=0, command=addTask)
button.place(x=0, y=520)

frame1 = Frame(root, bd=3, width=700, height=280, bg="#7A7D2A")
frame1.pack(pady=(160, 0))

listbox = Listbox(frame1, font=('arial', 12), width=40, height=16, bg="#3A6B35", fg="white", cursor="hand2",
                  selectbackground="#3A6B35")
listbox.pack(side=LEFT, fill=BOTH, padx=2)

scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()

button_del = Button(text="DEL", font="arial 20 bold", width=6, bg="#CBD18F", fg="#3A6B35", bd=0, command=deleteTask)
button_del.place(x=300, y=520)

button_done = Button(text="Done", font="arial 20 bold", width=6, bg="#CBD18F", fg="#3A6B35", bd=0, command=markComplete)
button_done.place(x=150, y=520)

button_completed = Button(text="Completed", font="arial 20 bold", width=10, bg="#CBD18F",fg="#3A6B35", bd=0, command=showCompletedList)
button_completed.place(x=225, y=600)

root.mainloop()