from tkinter import *
import tkinter.scrolledtext as scrl
from tkinter import messagebox
import tkinter.filedialog as tkfd


def showAbout():
    helloText = "Hello World"
    messagebox.showinfo("", helloText)

# SAVE

def saveAs():
    fileContent = content.get(1.0, END)

    fileName = tkfd.asksaveasfile(mode='w', defaultextension=".txt", filetypes = (("Text file", "*.txt"), ("All files", "*.*")))


    if fileName:
        fileName
    fileName.write(fileContent)
    fileName.close()

# OPEN
def openFile():
    try:
        file = tkfd.askopenfile(mode='r')
        fileContent = file.read()
    except:
        messagebox.warning("Unavailable")

# CLOSE

def exit():
	if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
		root.destroy()


#GUI
root = Tk()
root.title("Python Notepad")
root.geometry("640x480")


frame1 = Frame(
    master = root
)
frame1.pack(fill='both', expand='yes')


# MENU
menuBar = Menu(root)
root.config(menu = menuBar)


fileMenu = Menu(menuBar, tearoff = 0)
fileMenu.add_command(label = 'Open a file...', command = openFile)
fileMenu.add_command(label = 'Save to a file...', command = saveAs)
menuBar.add_cascade(label = 'File', menu = fileMenu)
fileMenu.add_separator()
fileMenu.add_command(label = 'Close', command = exit)


# RUN
root.mainloop()