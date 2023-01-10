# startwindow.py
from app.view.window import Window
import tkinter as tk


class StartWindow(Window):
    def __init__(self, controller):
        super.__init__()
        
        self.frameMain = tk.Frame(master=self.window)
        
        self.buttonCompletionForm = tk.Button(
            master=self.frameMain
            text="Completion Form"
            command=getCompletionForm
        )
        self.buttonEditForm = tk.Button(
            master=self.frameMain
            text="Edit Form"
            command=getEditForm
        )
        
        self.buttonCompletionForm.grid(
            column=0,
            row=0,
            padx=10,
            pady=10
        )
        
        self.buttonCompletionForm.grid(
            column=0,
            row=0,
            padx=10,
            pady=10
        )
        
        self.frameMain.pack()
        
    def getCompletionForm(self, controller):
        self.controller.getCompletionForm()
    
    def getEditForm(self, controller):
        self.controller.getEditForm()


if __name__ == "__main__":
    pass