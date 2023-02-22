# menuframe.py
from openaiclient.view.frame.baseframe import BaseFrame
import tkinter as tkinter


class MenuFrame(BaseFrame):
    def __init__(self, main, controller):
        super().__init__(main, controller)

        self.menuLabels = dict()
        self.menuOptions = dict()
        self.column = 0
        self.row = 0

    """
    def create(self):
        for menu in self.menuLabels:
            self.menuOptions[menu] = tk.StringVar()

            tk.OptionMenu(
                container=self,
                variable=self.menuOptions[menu],
                default=self.menuLabels[menu][0],
                *self.menuLavels[menu],
                # command=,
                # **kwargs
            ).grid(
                column=self.column,
                row=self.row,
                padx=10,
                pady=10,
            )

            self.column += 1

    # attach a frame to the menu frame
    def attach(self, frame):
        # if the current menu frame is
        # not the owner of the attached
        # frame, then it cannot attach it.
        if frame.master is self:
            frame.grid(
                column=0,
                row=1,
                padx=10,
                pady=10,
            )
        else:
            return RuntimeError()
    """
