import tkinter as tk
w = tk.Tk()
w.title('Window 1')
def func():
    return w.destroy
button = tk.Button(w, text='Click Me',bg='black',activebackground='gray',fg='white',activeforeground='red',width=15,command=func())
button.place(x=20,y=50)

w.mainloop()
