import tkinter
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title('To-Do-List')

def add_task():
    task = entry_task.get()
    if task != '':
        listbox_task.insert(tkinter.END, task)
        entry_task.delete(0,tkinter.END)
    else: tkinter.messagebox.showwarning(title = 'Warning', message='You must Enter something')

def del_task():
    try:
        task_ind = listbox_task.curselection()[0]
        listbox_task.delete(task_ind)
    except:
        tkinter.messagebox.showwarning(title = 'Warning', message='You must select something')


def load_task():
    try:
        task = pickle.load(open('E:\\Projects\\To-Do-List\\tasks.txt', 'rb'))
        listbox_task.delete(0, tkinter.END)
        for t in task:
            listbox_task.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title = 'Warning', message="Didn't saved the previous task")

def save_task():
    tasks = listbox_task.get(0, listbox_task.size())
    pickle.dump(tasks, open('E:\\Projects\\To-Do-List\\tasks.txt', 'wb'))

# create GUI
frame_task = tkinter.Frame(root)
frame_task.pack()

# creating list box
listbox_task = tkinter.Listbox(frame_task, height=15, width=50)
listbox_task.pack(side=tkinter.LEFT)

# create a scroll Bar
scroll_bar_task = tkinter.Scrollbar(frame_task)
scroll_bar_task.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_task.config(yscrollcommand = scroll_bar_task.set)
scroll_bar_task.config(command=listbox_task.yview)

# entry bars
entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

button_delete_task = tkinter.Button(root, text='ADD TACK', width=48, command=add_task)
button_delete_task.pack()

button_add_task = tkinter.Button(root, text='DELETE TASK', width=48, command=del_task)
button_add_task.pack()

button_load_task = tkinter.Button(root, text='LOAD TACK', width=48, command=load_task)
button_load_task.pack()

button_save_task = tkinter.Button(root, text='SAVE TACK', width=48, command=save_task)
button_save_task.pack()


root.mainloop()