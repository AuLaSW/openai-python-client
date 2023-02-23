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
        
        text = self.createHeaderText(row, col)
        
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

        #compLine = "The completion model can take text\nand generate novel outputs based\non your prompts."
        
        comp = self.createDescriptionText(compLine.strip())
        
        comp.grid(
            column=col,
            row=row,
            padx=15,
            pady=5,
            sticky=tk.W
        )
        
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
        
        #editLine = "The edit model takes both an\ninstruction and an input, editing\nthe input based on the instructions."
        
        edit = self.createDescriptionText(editLine.strip())
        
        edit.grid(
            column=col,
            row=row,
            padx=15,
            pady=5,
            sticky=tk.W
        )
        
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
        
        self.master.update()

        return self

    def createHeaderText(self, row, col):
        tk.Label(
            self,
            text="OpenAI Client",
            font=("", 16, "bold italic")
        ).grid(
            column=col,
            row=row,
            padx=0,
            pady=0,
            columnspan=2,
        )
        
        +row
        
        tk.Label(
            self,
            text="An open-source client for accessing the OpenAI API",
            font=("", 12, "italic")
        ).grid(
            column=col,
            row=row,
            padx=0,
            pady=0,
            columnspan=2,
        )
    
    def createDescriptionText(self, line):
        text = tk.Label(
            self,
            text=line,
            font=("", 10, ""),
            justify=tk.LEFT
        )
        
        return text

    def countLines(self, text):
        return text.count("1.0", "end", "displaylines")[0]

"""
Maximum length of labels:
+++++++++1+++++++++2+++++++++3++++5~~
"""

compLine = """
The completion models can take text
and generate novel outputs based on
your prompts.
"""

editLine = """
The edit model takes both an
instruction and an input, editing
the input based on the instructions.
"""

codexLine = """
The codex model generates code
based on a given input.
"""