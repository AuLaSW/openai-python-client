"""
This module creates windows for the openai-client program.
"""
from __future__ import annotations
import tkinter as tk
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
from openaiclient.view.frame.settings.completionsettings import CompletionSettings
from openaiclient.view.frame.settings.settingsframe import SettingsFrame
from openaiclient.view.frame.input.completioninput import CompletionInputFrame
from openaiclient.view.frame.menuframe import *

if TYPE_CHECKING:
    from openaiclient.controller.controller import Controller

class Window(ABC):
    """
    An abstract constructor class for different windows
    """
    def __init__(self, window: tk.Tk, controller: Controller):
        self._window = window
        self._controller = controller

    @abstractmethod
    def windowConstructor(self):
        """Constructs the frame product"""
        pass

    def draw(self):
        """Packs the product onto the window and starts the window"""
        frame = self.windowConstructor()
        frame.create()
        frame.pack()

        self.window.mainloop()

    @property
    def window(self):
        return self._window

    @property
    def controller(self):
        return self._controller


class CompletionSettingsWindow(Window):
    """
    A concrete factory class for the CompletionSettings window.
    """

    def windowConstructor(self) -> CompletionSettings:
        """Constructs a CompletionSettings frame product"""
        return CompletionSettings(self.window, self.controller)


class SettingsWindow(Window):
    """
    A concrete factory class for the CompletionSettings window.
    """

    def windowConstructor(self) -> SettingsFrame:
        """Constructs a CompletionSettings frame product"""
        return SettingsFrame(self.window, self.controller)


class CompletionInputWindow(Window):
    """
    A concrete factor class for the CompletionInput window.
    """

    def windowConstructor(self) -> CompletionInputFrame:
        menu = MainMenu(self.window)
        menu.create()
        self.window.config(menu=menu.menubar)
        return CompletionInputFrame(self.window, self.controller)

    def draw(self):
        frame = self.windowConstructor()
        frame.create()
        frame.pack()

        self.window.mainloop()


if __name__ == "__main__":
    from openaiclient.controller.controller import Controller
    from tests.unit.fixture import api

    window = tk.Tk()
    controller = Controller(api)

    csw = CompletionInputWindow(window, controller)

    csw.draw()
