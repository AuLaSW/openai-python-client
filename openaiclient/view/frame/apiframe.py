"""
APIFrame class
"""
from increment import Increment
import tkinter as tk
from tkinter import ttk
from openaiclient.view.frame import BaseFrame
from tests.unit.fixture import api


class APIFrame(BaseFrame):
    """
    A class for creating the frame for the API window when no
    API key is discovered on startup
    """
    
    def __init__(self, main, controller):
        super().__init__(main, controller)

    def create(self):
        col = Increment()
        row = Increment()
        
        tempFrame1 = tk.Frame(self.master)
        
        tempCol = Increment()
        tempRow = Increment()
        
        self.addHorizSeparator(tempCol, tempRow, tempFrame1)
        
        tk.Label(
            tempFrame1,
            text=instruction.strip(),
            justify=tk.LEFT,
            font=("", 10, ""),
        ).grid(
            column=tempCol,
            row=tempRow,
            padx=10,
            columnspan=2
        )
        
        ~tempCol
        +tempRow
        
        self.addHorizSeparator(tempCol, tempRow, tempFrame1)
        
        tempFrame1.grid(
            column=col,
            row=row,
            columnspan=2
        )
        
        ~tempCol
        ~tempRow
        
        ~col
        +row
        
        tempFrame2 = tk.Frame(self.master)
        
        tempCol = Increment()
        tempRow = Increment()
        
        tk.Button(
            tempFrame2,
            text="Generate API Key",
            font=("", 10, ""),
            command=self.setAPI
        ).grid(
            column=tempCol,
            row=tempRow,
            padx=10,
            pady=(5,5),
            ipadx=2
        )
        
        +tempCol
        
        tk.Button(
            tempFrame2,
            text="Use Test API",
            font=("", 10, ""),
            command=self.setTestAPI
        ).grid(
            column=tempCol,
            row=tempRow,
            padx=10,
            pady=(5,5),
            ipadx=2
        )
        
        tempFrame2.grid(
            column=col,
            row=row,
            columnspan=2
        )
        
        ~col
        +row
        
        tk.Label(
            self,
            text="API Key:",
            font=("", 10, ""),
        ).grid(
            column=col,
            row=row,
            pady=(5,10),
            padx=(10,5),
        )
        
        +col
        
        tk.Entry(
            self,
            width=30
        ).grid(
            column=col,
            row=row,
            pady=10,
            padx=(5,10),
        )
        
        ~col
        +row
        
        tk.Button(
            self,
            text="Save API Key",
            width=30
        ).grid(
            column=col,
            row=row,
            pady=10,
            padx=10,
        )
    
    def addHorizSeparator(self, col, row, frame):
        ~col
        
        ttk.Separator(
            frame,
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
    
    def setAPI(self):
        pass

    def setTestAPI(self):
        self.controller._api = api
        self.master.destroy()


instruction="""
If you would like to use OpenAI's API,
please log into your account and generate
the API key there, then paste the API key
into the designated space below. 

You can also click the "Generate API Key"
below to open the login link to get the 
API key.

If you just want to test out the application, 
select the "Use Test API" button below.
"""