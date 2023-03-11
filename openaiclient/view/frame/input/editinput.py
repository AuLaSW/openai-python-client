"""
CompletionInput class
"""
import tkinter as tk
from tkinter import ttk
from increment import Increment
from openaiclient.view.frame.baseframe import BaseFrame


class EditInputFrame(BaseFrame):
    def __init__(self, main, controller):
        super().__init__(main, controller)

        self.controller.editRequest()
        self._input = tk.Text(
            self,
            width=50,
            height=30
        )

        self._instruction = tk.Text(
            self,
            width=50,
            height=3
        )

    def create(self):
        row = Increment()
        col = Increment()

        self.addHorizSeparator(col, row)

        tk.Label(
            self,
            text="Edit Endpoint",
            font=("", 14, "")
        ).grid(
            column=col,
            row=row,
            pady=0
        )

        +row

        self.addHorizSeparator(col, row)

        """
        tk.Button(
            self,
            text="test"
        ).grid(
            column=col,
            row=row,
            pady=10,
            padx=10,
            sticky=tk.W
        )
        """

        +row

        tk.Label(
            master=self,
            text="Enter Instructions:"
        ).grid(
            column=col,
            row=row,
            padx=10,
            sticky=tk.W+tk.S
        )

        +row

        self._instruction.grid(
            column=col,
            row=row,
            padx=10,
            pady=5
        )

        +row

        tk.Label(
            master=self,
            text="Enter Input:"
        ).grid(
            column=col,
            row=row,
            padx=10,
            sticky=tk.W+tk.S
        )

        +row

        self._input.grid(
            column=col,
            row=row,
            padx=10,
            pady=5
        )

        """
        self._prompt.bind(
            "<Any-KeyPress>",
            self.underlineUpdate
        )
        """

        +row

        tk.Button(
            master=self,
            text="Send",
            command=self.sendInput
        ).grid(
            column=col,
            row=row,
            padx=10,
            pady=10,
            ipadx=40
        )

        self.tags()

        return self

    def addHorizSeparator(self, col, row):
        ~col

        ttk.Separator(
            self,
            orient="horizontal",
        ).grid(
            column=col,
            row=row,
            columnspan=2,
            sticky=tk.W + tk.E,
            padx=10,
            pady=5
        )

        +row

    def tags(self):
        pass
    """
        self._prompt.tag_add(
            "testTag",
            1.0,
            tk.END,
        )

        self._prompt.tag_bind(
            "testTag",
            "<Any-KeyPress>",
            self.underlineUpdate
        )

    def underlineUpdate(self, event):
        self._prompt.tag_add(
            "testTag",
            1.0,
            tk.END,
        )

        self._prompt.tag_configure(
            tagName="testTag",
            underline=1
        )
    """

    @property
    def text(self):
        return self._prompt.get(
            index1=1.0,
            index2=tk.END
        )

    @text.setter
    def text(self, val):
        self._prompt.replace(
            index1=1.0,
            index2=tk.END,
            chars=val
        )

    def sendInput(self):
        self.controller.handler.setPrompt(self.text)
        self.controller.getResponse()
        self.text = self.controller.response.text.strip()
        self.tags()


if __name__ == "__main__":
    from openaiclient.controller.controller import Controller
    from openaiclient.view.view import View
    from tests.unit.fixture import api

    controller = Controller(api)
    controller.completionRequest()
    window = tk.Tk()
    controller.view.completionInputWindow(window)
