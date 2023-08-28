from tkinter import *
root=Tk()

root.title('CALCULATOR')
root.geometry('300x100')

def calculate():
    result=eval(entry.get())
    label.config(text='Result:' + str(result))
    
entry=Entry(root)
entry.pack()

button=Button(root, text='Calculate', command=calculate)
button.pack()

label=Label(root, text='Result:')
label.pack()

root.mainloop()