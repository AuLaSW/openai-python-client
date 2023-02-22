"""
mainframe module
"""
import tkinter as tk
from openaiclient.view.frame.baseframe import BaseFrame


class MainFrame(BaseFrame):
    """
    This class creates the frame generated when the
    application first starts.
    """
    
    def __init__(self, window, controller) -> None:
        super().__init__(window, controller)
    
    def create(self) -> BaseFrame:
        self.createText().grid(
            column=0,
            row=0,
            columnspan=2
        )
        
        tk.Button(
            text="Completion Endpoint",
            command=self.controller.view.completionInputWindow
        ).grid(
            column=0,
            row=1,
            padx=10,
            pady=10
        )
        
        tk.Button(
            text="Edit Endpoint",
            state=tk.DISABLED
        ).grid(
            column=1,
            row=1,
            padx=10,
            pady=10
        )
        
        return self
        
        
    def createText(self):
        text = tk.Text(
            width=30,
            background=self.master['background'],
            padx=15,
            pady=15,
            relief=tk.FLAT,
            wrap=tk.WORD,
        )
        
        line = "Hello! And welcome to openaiclient!\n\nPlease select an option below:"

        text.insert(
            1.0,
            line,
        )
        
        font = ("Times New Roman", 15, "")
        text.configure(font=font)

        text.tag_add(
            "testTag",
            1.0,
            "1.6",
        )

        text.tag_configure(
            tagName="testTag",
            font="Times 15 bold",
        )
        
        text['state'] = tk.DISABLED
        text['height'] = self.countLines(line)

        return text

    def countLines(self, text):
        count = 0

        for line in text.splitlines():
            count += 1

        return count