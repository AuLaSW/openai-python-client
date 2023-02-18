"""
This module contains the class View, which is part of the MVC pattern for the
openai-client application.

API:
    run():
        Creates the window and starts the mainloop() for it.
"""
from openaiclient.view.window.window import Window


class View:
    """
    Class View:

    Manages the GUI, interacts with the Controller and Model classes.

    This class uses tkinter to generate the GUI.
    """

    def __init__(self, controller):
        # bind the controller to the view object
        # by passing the controller to the view,
        # we can bind controller functions to view
        # functions
        self.controller = controller

        # the Window class will be directly
        # interacting with the tkinter package
        # this will give us specific frames and
        # windows to call and use without having
        # to go through tkinter directly
        self.window = Window(self.controller)

    def run(self):
        """Run the start window and start the mainloop."""
        self.window.completionSettingsWindow()
        self.window.window.mainloop()


if __name__ == "__main__":
    from openaiclient.controller import Controller

    tempController = Controller()

    view = View(tempController)

    view.run()
