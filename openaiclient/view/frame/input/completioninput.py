"""
CompletionInput class
"""
import tkinter as tk
from openaiclient.view.frame.baseframe import BaseFrame


class CompletionInputFrame(BaseFrame):
    def __init__(self, main, controller):
        super().__init__(main, controller)

        self.controller.compReq()
        self._prompt = tk.Text(self)

    def create(self):
        self._prompt.grid(
            column=0,
            row=0,
            padx=10,
            pady=10
        )

        tk.Button(
            master=self,
            text="Send",
            command=self.sendInput
        ).grid(
            column=0,
            row=1,
            padx=10,
            pady=10
        )

    @property
    def text(self):
        return self._prompt.get(
            index1=1.0,
            index2=tk.END
        )

    @text.setter
    def text(self, val):
        self._prompt.insert(
            index=1.0,
            chars=val
        )

    def sendInput(self):
        self.controller.request.set_prompt(self.text)
        self.controller.request.getResponse()


if __name__ == "__main__":
    from openaiclient.controller.controller import Controller

    window = tk.Tk()
    controller = Controller(None)

    cif = CompletionInputFrame(
        main=window,
        controller=controller
    )

    cif.create()
    cif.pack()

    window.mainloop()
