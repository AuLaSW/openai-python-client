"""
CompletionInput class
"""
import tkinter as tk
from openaiclient.view.frame.baseframe import BaseFrame


class CompletionInputFrame(BaseFrame):
    def __init__(self, main, controller):
        super().__init__(main, controller)

        self.controller.compReq()
        self._prompt = tk.Text(
            self,
            width=50,
            height=30
        )

    def create(self):
        self._prompt.grid(
            column=0,
            row=0,
            padx=10,
            pady=10
        )

        self._prompt.bind(
            "<Any-KeyPress>",
            self.underlineUpdate
        )

        tk.Button(
            master=self,
            text="Send",
            command=self.sendInput
        ).grid(
            column=0,
            row=1,
            padx=10,
            pady=10,
            ipadx=40
        )

        self.tags()

    def tags(self):
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
        self.controller.request.set_prompt(self.text)
        self.controller._response = self.controller.request.getResponse()
        self.text = self.controller._response.text
        self.tags()


if __name__ == "__main__":
    from openaiclient.controller.controller import Controller
    from tests.unit.fixture import api

    window = tk.Tk()
    window.resizable(False, False)
    controller = Controller(api)

    cif = CompletionInputFrame(
        main=window,
        controller=controller
    )

    cif.create()
    cif.pack()

    window.mainloop()
