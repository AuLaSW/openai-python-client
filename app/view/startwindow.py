# startwindow.py
from window import Window
import tkinter as tk


class StartWindow(Window):
    # def __init__(self, controller):
    def __init__(self):
        super().__init__(None)

        self.frameMain = tk.Frame(master=self.window)

        self.buttonCompletionForm = tk.Button(
            master=self.frameMain,
            text="Completion Form",
            command=self.getCompletionForm
        )
        self.buttonEditForm = tk.Button(
            master=self.frameMain,
            text="Edit Form",
            command=self.getEditForm
        )

        self.buttonCompletionForm.grid(
            column=0,
            row=0,
            padx=10,
            pady=10
        )

        self.buttonEditForm.grid(
            column=1,
            row=0,
            padx=10,
            pady=10
        )

        self.frameMain.pack()

    def getCompletionForm(self):
        # self.controller.getCompletionForm()
        pass

    def getEditForm(self):
        # self.controller.getEditForm()
        pass


if __name__ == "__main__":
    window = StartWindow()
    window.init()
