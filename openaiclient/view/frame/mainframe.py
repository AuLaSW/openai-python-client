"""
mainframe module
"""
import tkinter as tk
from tkinter import ttk
import math
from increment import Increment
from openaiclient.view.frame.baseframe import BaseFrame


class MainFrame(BaseFrame):
    """
    This class creates the frame generated when the
    application first starts.
    """

    def __init__(self, window, controller) -> None:
        super().__init__(window, controller)

    def create(self) -> BaseFrame:
        col = Increment()
        row = Increment()
        
        self.createText().grid(
            column=col,
            row=row,
            columnspan=2
        )
        
        +row
        
        ttk.Separator(
            self,
            orient="horizontal",
        ).grid(
            column=col,
            row=row,
            columnspan=2,
            sticky=tk.W+tk.E,
            padx=10,
            pady=5
        )
        
        +row
        
        comp = tk.Text(
            self,
            width=30,
            background=self.master['background'],
            padx=0,
            pady=0,
            relief=tk.FLAT,
            wrap=tk.WORD,
        )
        
        comp.grid(
            column=col,
            row=row,
            padx=15,
            pady=5,
            sticky=tk.W
        )
        
        compLine = "This gives you access to the completion endpoint"
        
        comp.insert(
            1.0,
            compLine,
        )
        
        self.master.update()
        
        comp['height'] = comp.count("1.0", "end", "displaylines")[0]
        
        +col

        tk.Button(
            self,
            text="Completion Endpoint",
            command=self.controller.view.completionInputWindow,
            width=20,
            height=2
        ).grid(
            column=col,
            row=row,
            padx=15,
            pady=5   
        )

        ~col
        +row
        
        edit = tk.Text(
            self,
            width=30,
            background=self.master['background'],
            padx=0,
            pady=0,
            relief=tk.FLAT,
            wrap=tk.WORD,
        )
        
        edit.grid(
            column=col,
            row=row,
            padx=15,
            pady=5,
        )
        
        editLine = "This gives you access to the edit endpoint"
        
        edit.insert(
            1.0,
            editLine,
        )
        
        self.master.update()
        
        edit['height'] = edit.count("1.0", "end", "displaylines")[0]
        
        +col

        tk.Button(
            self,
            text="Edit Endpoint",
            state=tk.DISABLED,
            width=20,
            height=2
        ).grid(
            column=col,
            row=row,
            padx=15,
            pady=5
        )

        return self

    def createText(self):
        text = tk.Text(
            self,
            width=30,
            background=self.master['background'],
            padx=15,
            pady=15,
            relief=tk.FLAT,
            wrap=tk.WORD,
        )

        line = "Hello! And welcome to openaiclient!"

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
