import tkinter as tk
import datetime 


root = tk.Tk()
root.title("First")
root.geometry("400x400")

def secure_window(foo):
    def login():
        if entr.get() == "admin" and entr2.get() == "admin":
            foo()
            new_win.destroy()  
        else:
            lbl.config(text="Invalid login or password")

    new_win = tk.Toplevel(root)
    new_win.title("Secure Window")
    new_win.geometry("200x200")

    login_label = tk.Label(new_win, text="Entry login")
    login_label.pack()
    entr = tk.Entry(new_win)
    entr.pack()

    passw_label = tk.Label(new_win, text="Entry pass")
    passw_label.pack()
    entr2 = tk.Entry(new_win, show="*")
    entr2.pack()

    bth = tk.Button(new_win, text="Login", command=login)
    bth.pack()


def checker(foo):
    def wrapper():
        secure_window(foo)
    return wrapper

def check():
    lbl.config(text="Ok")

time = datetime.datetime.now()
@checker
def check2():
    lbl.config(text=f"Привет, Игорь, сейчас время {time}")

test = tk.Button(root, text="Test bez auth", command=check)
test.pack()

test2 = tk.Button(root, text="Test s auth", command=check2)
test2.pack()

lbl = tk.Label(root, text="Status")
lbl.pack()

root.mainloop()
