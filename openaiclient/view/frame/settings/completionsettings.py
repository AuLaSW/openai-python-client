# completionsettings.py
from openaiclient.view.frame.settings \
    .settingsframe import SettingsFrame

"""
Class CompletionSettings:

This class is a child of SettingsFrame and implements a setting frame
with settings for an OpenAI API text-completion request.
"""


class CompletionSettings(SettingsFrame):
    def __init__(self, main, controller):
        super().__init__(main, controller)

        self.settings = self.controller.request.settings
        print(self.settings)


if __name__ == "__main__":
    import tkinter as tk
    from openaiclient.controller.controller import Controller
    from tests.unit.fixture import api

    window = tk.Tk()
    controller = Controller(api)
    controller.compReq()

    frame = CompletionSettings(
        main=window,
        controller=controller
    )

    frame.create()

    frame.pack()

    window.mainloop()
