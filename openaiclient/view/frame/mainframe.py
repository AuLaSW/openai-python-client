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
        
        text = self.createHeaderText(col, row)
        
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
        
        comp = self.createEntryButton(
            compLine.strip(),
            "Completion Endpoint",
            self.controller.view.completionInputWindow,
            col=col,
            row=row
        )
        
        ~col
        +row
        
        edit = self.createEntryButton(
            editLine.strip(),
            "Edit Endpoint",
            None,
            col=col,
            row=row
        )
        
        ~col
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

        self.master.update()

        return self

    def createHeaderText(self, col, row):
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
        
        +row
    
    def createEntryButton(self, line, label, func, col, row):
        tk.Label(
            self,
            text=line,
            font=("", 10, ""),
            justify=tk.LEFT
        ).grid(
            column=col,
            row=row,
            padx=15,
            pady=5,
            sticky=tk.W
        )
        
        +col

        tk.Button(
            self,
            text=label,
            command=func,
            width=20,
            height=2
        ).grid(
            column=col,
            row=row,
            padx=15,
            pady=5   
        )

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