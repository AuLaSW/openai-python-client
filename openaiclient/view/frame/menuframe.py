# menuframe.py
import tkinter as tk
from openaiclient.view.frame.baseframe import BaseFrame


class MenuFrame(BaseFrame):
    def __init__(self, main, controller):
        super().__init__(main, controller)

        self.menuLabels = {}
        self.menuOptions = {}
        self.column = 0
        self.row = 0

    def create(self):
        mb = tk.Menubutton(
            self,
            text='Test Menu',
            relief=tk.RAISED
        )

        mb.grid(
            sticky=tk.W
        )

        mb.menu = tk.Menu(
            mb,
            tearoff=0
        )
        mb['menu'] = mb.menu


        mb.menu.add_command(
            label='test command',
            command=None
        )

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


if __name__ == "__main__":
    """
    An example of how to create a menu
    """
    window = tk.Tk()
    mb = tk.Menubutton(
        window,
        text='condiments',
    )
    mb.grid()

    mb.menu = tk.Menu(
        mb,
        tearoff=0
    )
    mb['menu'] = mb.menu
    mayoVar = tk.IntVar()
    ketchVar = tk.IntVar()
    mb.menu.add_checkbutton(
        label='mayo',
        variable=mayoVar
    )
    mb.menu.add_command(
        label='ketchup',
        command=None
    )

    window.mainloop()
