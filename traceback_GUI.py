import tkinter as tk
import re
import Traceback


### TO-DO : pop-up menu


def caller(event):
    if checkVar.get() != 0:
        end = re.compile(r'at\s+[^\n\r]*')
    else:
        end = re.compile(r'\+[0-9]{1,5}\sat\s+[^\n\r]*')

    workfile = textBox.get("1.0","end-1c")
    data = workfile.split("\n")

    startlist, endlist = Traceback.trim(data, end)
    matches = Traceback.find_function(data, startlist, endlist)

    window = tk.Toplevel(root)
    display = tk.Text(window)
    display.insert("insert", matches)
    display.pack()



root = tk.Tk()
checkVar = tk.IntVar()


## FRAMES ##
topFrame = tk.Frame(root)
topFrame.pack()

bottomFrame = tk.Frame(root)
bottomFrame.pack(side="bottom")


## TEXT-BOXES ##
textBox = tk.Text(topFrame, height=30, width=130)
textBox.pack(side="top")


## BUTTONS ##
button_addNums = tk.Checkbutton(bottomFrame, text="Include function numbers", variable = checkVar, onvalue = 1, offvalue = 0)

button_run = tk.Button(bottomFrame, text="Run", fg="red")
button_run.bind("<Button-1>", caller)

button_addNums.pack(side="left")
button_run.pack(side="right")




root.mainloop()