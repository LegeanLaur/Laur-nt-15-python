import tkinter
import tkinter.messagebox
import pickle
import login_system


window = tkinter.Tk()
window.title("ToDo List")

def add_task():
    task = entry_task.get()
    if task != "":
      listbox_tasks.insert(tkinter.END, task)
      entry_task.delete(0, tkinter.END) # Must rewrite the task if i want to add it again
    else:
      tkinter.messagebox.showwarning(title="Warning", message="Please enther a task!")

def delete_task():
    try:
       task_index = listbox_tasks.curselection()[0]  # select only 1 item
       listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task")
def load_tasks():
    try:
        tasks = pickle.load(open("tasks.datafile", "rb"))
        for task in tasks:  # each task we load it
            listbox_tasks.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="Cannot find task.datafile")
def save_tasks():
    tasks  = listbox_tasks.get(0, listbox_tasks.size()) # tasks that are in the listbox
    pickle.dump(tasks,open("tasks.datafile", "wb"))

frame_tasks = tkinter.Frame(window)
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height=3, width=50)
listbox_tasks.pack()

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT,fill = tkinter.Y) # Scrollbar location and display

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview) # scrollbar working

entry_task = tkinter.Entry(window, width = 50)
entry_task.pack()

button_add_task = tkinter.Button(window, text ="Add task",font=("Times New Roman",10), background="chartreuse", width = 48, command = add_task)
button_add_task.pack()

button_delete_task = tkinter.Button(window, text = "Delete task",font=("Times New Roman",10), background="red", width = 48, command = delete_task)
button_delete_task.pack()

button_load_tasks = tkinter.Button(window, text ="Load tasks",font=("Times New Roman",10), background="aqua", width = 48, command = load_tasks)
button_load_tasks.pack()

button_save_tasks = tkinter.Button(window, text ="Save task",font=("Times New Roman",10),background="yellow", width = 48, command = save_tasks)
button_save_tasks.pack()

window.mainloop()
