import tkinter as tk

def answer():
    a = my_entry.get()
    result.config(text=a, fg='green', font='Arial')
parent = tk.Tk()
result = tk.Label(parent )
answer = tk.Button(parent,text='вывести', command=answer)


my_entry = tk.Entry(parent)



my_entry.pack()
result.pack()
answer.pack()

parent.mainloop()
