from tkinter import *
from tkinter import filedialog, ttk
from Float_Arithmetic import *

window = Tk()

window.geometry("700x700")
window.title('Float Arithmetic Compression SIM')
icon = PhotoImage(file='Float_Arithmetic/image.png')
window.iconphoto(True,icon)
window.config(background='black')

def open_file():
    file_path = filedialog.askopenfilename()
    print(f"File opened: {file_path}")

open_file_button = Button(window,
                          text='Open File',
                          command=open_file,
                          font=('Comic Sans', 14),
                          fg='green',
                          bg='black',
                          activeforeground='green',
                          activebackground='black')
open_file_button.pack()

def save_file():
    file = filedialog.asksaveasfile(defaultextension=".txt",
                                    filetypes=[("Text files", "*.txt"), 
                                               ("All files", "*.*")])
    if file:
        file.write("Sample text")
        file.close()

save_file_button = Button(window,
                          text='Save File',
                          command=save_file,
                          font=('Comic Sans', 14),
                          fg='green',
                          bg='black',
                          activeforeground='green',
                          activebackground='black')
save_file_button.pack()

window.mainloop()