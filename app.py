import tkinter as tk 
import subprocess

root = tk.Tk()

root.title("First")
root.geometry("400x400")



def open_win_py():
    subprocess.Popen(["python3", "win.py"])

def check_user():
    gett = entr.get()
    gett2 = entr2.get()
    if gett == "admin" and gett2 == "admin":
        lbl3.config(text="OK")        
        open_win_py()  
        root.destroy()
    else:
        lbl3.config(text="No ok")
    

login = tk.Label(text="Entry login")
login.pack()
entr = tk.Entry()
entr.pack()
passw = tk.Label(text="Entry pass")
passw.pack()
entr2 = tk.Entry(show="*")
entr2.pack()
bth = tk.Button(text="Login", command=check_user)
bth.pack()
lbl3 = tk.Label(text="status")
lbl3.pack()


root.mainloop()

