# menuframe.py
import tkinter as tk
from openaiclient.view.frame.baseframe import BaseFrame


class MenuFrame(BaseFrame):
    def __init__(self, main, controller):
        super().__init__(main, controller)

        self.menuLabels = {}
        self.menuOptions = {}
        self.column = 0
        self.row = 0

    def create(self):


if __name__ == "__main__":
    """
    An example of how to create a menu
    """
    from tkinter import *

    def donothing():
        # Toplevel() is preferred over generating
        # a new Tk() instance
        filewin = Toplevel(root)
        button = Button(filewin, text="Do nothing button")
        button.pack()

    # generate the root Tk() instance
    root = Tk()
    # attach a Menu to the root instance
    # this menu will act as the menu bar that
    # all of the other menus branch off from
    menubar = Menu(root)
    # create the file menu
    filemenu = Menu(menubar, tearoff=0)
    # add commands to the file menu
    filemenu.add_command(label="New", command=donothing)
    filemenu.add_command(label="Open", command=donothing)
    filemenu.add_command(label="Save", command=donothing)
    filemenu.add_command(label="Save as...", command=donothing)
    filemenu.add_command(label="Close", command=donothing)

    # this adds a separator between Close and '
    # Exit buttons in the file menu
    filemenu.add_separator()

    filemenu.add_command(label="Exit", command=root.quit)
    
    # now, add the file menu to the menubar
    # and add it as a cascade menu
    menubar.add_cascade(label="File", menu=filemenu)
    
    # create the edit menu
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Undo", command=donothing)

    editmenu.add_separator()

    editmenu.add_command(label="Cut", command=donothing)
    editmenu.add_command(label="Copy", command=donothing)
    editmenu.add_command(label="Paste", command=donothing)
    editmenu.add_command(label="Delete", command=donothing)
    editmenu.add_command(label="Select All", command=donothing)

    # add the edit menu to the menu bar
    menubar.add_cascade(label="Edit", menu=editmenu)
    
    # create the help menu
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=donothing)
    helpmenu.add_command(label="About...", command=donothing)
    
    # add the edit menu to the menubar
    menubar.add_cascade(label="Help", menu=helpmenu)

    # configure the root window to use
    # the menu bar as the menu
    root.config(menu=menubar)
    # run the root window
    root.mainloop()