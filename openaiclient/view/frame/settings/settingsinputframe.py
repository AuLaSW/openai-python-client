# settingsinputframe.py
import tkinter as tk
from openaiclient.view.frame.baseframe import BaseFrame


class SettingsInputFrame(BaseFrame):
    def __init__(self, main, controller, label, default):
        super().__init__(main, controller)

        # this should be handled by master in the
        # tk.Frame class
        # self.main = main
        self.label = label
        self.default = default