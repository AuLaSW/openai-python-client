"""
Input module
"""
import tkinter as tk
from openaiclient.view.frame.baseframe import BaseFrame


class Input(BaseFrame):
    def __init__(self, main, controller):
        super().__init__(main, controller)

        self._textBox = None

    def create(self):
        self._textBox = tk.Text(self)
        self._textBox.grid(
            column=0,
            row=0,
            padx=10,
            pady=10
        )

    @property
    def text(self):
        return self._textBox.get(
            index1=1.0,
            index2=tk.END
        )

    @text.setter
    def text(self, val):
        self._textBox.insert(
            index=0,
            chars=val
        )


if __name__ == "__main__":
    window = tk.Tk()

    inputFrame = Input(
        main=window,
        controller=None
    )

    inputFrame.create()

    inputFrame.pack()

    window.mainloop()
