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
    
    def setAttr(self, key, val):
        setter = getattr(self.controller.request, "set_"+key)
        
        if type(self.settings[key]).__name__ == "Model":
            model = getattr(self.controller.models, val.replace("-", "_"))
            setter(model)
        else:
            setter(type(val)(val))


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
