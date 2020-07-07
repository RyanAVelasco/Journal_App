from tkinter import *
from tkinter.scrolledtext import ScrolledText


def buttonSave():
    saveWindow = Tk()
    saveWindow.title("Save")
    saveWindow.geometry("500x100")
    saveLabel = Label(saveWindow, text="Enter filename below")
    saveScreen = Entry(saveWindow, text="save")
    saveLabel.pack()
    saveScreen.pack()
    saveWindow.mainloop()


def buttonConfirmation():
    pass


def buttonLoad():
    loadWindow = Tk()
    loadWindow.title("Load file")
    loadWindow.geometry("500x100")
    loadLabel = Label(loadWindow, text="Enter filename below")
    loadScreen = Entry(loadWindow, text="Load")
    loadLabel.pack()
    loadScreen.pack()
    loadWindow.mainloop()



def buttonClose():
    writeWindow.quit()


# windows
writeWindow = Tk()
writeWindow.title("Minimalistic Journal")
# loadWindow = Tk()
# confimationWindow = Tk()

# writeWindow
saveButton = Button(writeWindow, text="SAVE", command=lambda: buttonSave())
loadButton = Button(writeWindow, text="LOAD", command=lambda: buttonLoad())
closeButton = Button(writeWindow, text="CLOSE", command=lambda: buttonClose())

saveButton.grid(row=0, column=0, ipadx=15, ipady=5, pady=5)
loadButton.grid(row=0, column=1, ipadx=15, ipady=5, pady=5)
closeButton.grid(row=0, column=2, ipadx=15, ipady=5, pady=5)

ScrolledText(writeWindow).grid(row=1, columnspan=3, padx=15, pady=10)  # Journal entry section


# launch window
writeWindow.mainloop()
# loadWindow.mainloop()
# confimationWindow.mainloop()