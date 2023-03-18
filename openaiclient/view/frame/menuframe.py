# menuframe.py
from __future__ import annotations
from abc import ABC, abstractmethod
import tkinter as tk


class MenuFactory(ABC):
    """
    An abstract factory for generating menus
    """

    def __init__(self, root, controller):
        self._menubar = tk.Menu(root)
        self._controller = controller

        self.create()

    @property
    @abstractmethod
    def menubar(self):
        pass

    @abstractmethod
    def create(self):
        pass


class MainMenu(MenuFactory):
    """
    Creates a main menu
    """

    @property
    def menubar(self):
        return self._menubar

    def create(self) -> None:
        self.addFileMenu()

    def createFileMenu(self) -> tk.Menu:
        return MainFileMenu(self._menubar, self._controller).menu

    def addFileMenu(self):
        self._menubar.add_cascade(
            label="File",
            menu=self.createFileMenu(),
        )


class CompletionRequestMenu(MenuFactory):
    """
    Creates the menu when working with a completion request
    """

    @property
    def menubar(self):
        return self._menubar

    def create(self) -> None:
        self.addFileMenu()
        self.addSettingMenu()

    def createFileMenu(self) -> tk.Menu:
        return CompletionRequestFileMenu(
            self._menubar,
            self._controller
        ).menu

    def addFileMenu(self):
        self._menubar.add_cascade(
            label="File",
            menu=self.createFileMenu(),
        )

    def createSettingMenu(self) -> tk.Menu:
        return CompletionRequestSettingMenu(
            self._menubar,
            self._controller
        ).menu

    def addSettingMenu(self):
        self._menubar.add_cascade(
            label="Settings",
            menu=self.createSettingMenu(),
        )


class EditRequestMenu(MenuFactory):
    """
    Creates the menu when working with an edit request
    """
    
    @property
    def menubar(self):
        return self._menubar

    def create(self) -> None:
        self.addFileMenu()
        self.addSettingMenu()

    def createFileMenu(self) -> tk.Menu:
        return EditRequestFileMenu(
            self._menubar,
            self._controller
        ).menu

    def addFileMenu(self):
        self._menubar.add_cascade(
            label="File",
            menu=self.createFileMenu(),
        )

    def createSettingMenu(self) -> tk.Menu:
        return EditRequestSettingMenu(
            self._menubar,
            self._controller
        ).menu

    def addSettingMenu(self):
        self._menubar.add_cascade(
            label="Settings",
            menu=self.createSettingMenu(),
        )


class CodexRequestMenu(MenuFactory):
    """
    Creates the menu when working with a completion request
    """

    @property
    def menubar(self):
        return self._menubar

    def create(self) -> None:
        self.addFileMenu()
        self.addSettingMenu()

    def createFileMenu(self) -> tk.Menu:
        return CodexRequestFileMenu(
            self._menubar,
            self._controller
        ).menu

    def addFileMenu(self):
        self._menubar.add_cascade(
            label="File",
            menu=self.createFileMenu(),
        )

    def createSettingMenu(self) -> tk.Menu:
        return CodexRequestSettingMenu(
            self._menubar,
            self._controller
        ).menu

    def addSettingMenu(self):
        self._menubar.add_cascade(
            label="Settings",
            menu=self.createSettingMenu(),
        )


class AbstractMenuProduct(ABC):
    """
    An abstract menu class, parent to all menu product classes.
    """

    def __init__(self, menu, controller):
        self._menu = tk.Menu(
            menu,
            tearoff=0
        )
        self._controller = controller

        self.create()

    @abstractmethod
    def create(self):
        pass

    @property
    @abstractmethod
    def menu(self):
        pass


class DropdownMenu(AbstractMenuProduct):
    """
    Creates a dropdown menu for use inside of another menu
    """


class EndpointDropdownMenu(DropdownMenu):
    """
    Creates a dropdown menu for selecting the different endpoints
    """

    def create(self):
        pass

    def addCompletion(self):
        self._menu.add_command(
            label="Completion",
            command=self._controller.view.completionInputWindow
        )

    def addEdit(self):
        self._menu.add_command(
            label="Edit",
            command=self._controller.view.editInputWindow
        )

    def addCodex(self):
        self._menu.add_command(
            label="Codex",
            command=self._controller.view.codexInputWindow
        )

    @property
    def menu(self):
        return self._menu


class FileMenu(AbstractMenuProduct):
    """
    Abstract product for file menus
    """


class MainFileMenu(FileMenu):
    """
    Creates a file menu for the main menu
    """

    def create(self):
        endpointMenu = EndpointDropdownMenu(self.menu, self._controller)
        endpointMenu.addCompletion()
        endpointMenu.addEdit()
        endpointMenu.addCodex()
        endpointMenu = endpointMenu.menu
        self._menu.add_cascade(label="Change endpoint...", menu=endpointMenu)

    @property
    def menu(self):
        return self._menu


class CompletionRequestFileMenu(FileMenu):
    """
    Creates a file menu for the completion request view
    """

    def create(self):
        self._menu.add_command(label="Home",
                               command=self._controller.view.mainWindow)
        endpointMenu = EndpointDropdownMenu(self.menu, self._controller)
        endpointMenu.addEdit()
        endpointMenu.addCodex()
        endpointMenu = endpointMenu.menu
        self._menu.add_cascade(label="Change endpoint...", menu=endpointMenu)

    @property
    def menu(self):
        return self._menu


class EditRequestFileMenu(FileMenu):
    """
    Creates a file menu for the edit request view
    """

    def create(self):
        self._menu.add_command(label="Home",
                               command=self._controller.view.mainWindow)
        endpointMenu = EndpointDropdownMenu(self.menu, self._controller)
        endpointMenu.addCompletion()
        endpointMenu.addCodex()
        endpointMenu = endpointMenu.menu
        self._menu.add_cascade(label="Change endpoint...", menu=endpointMenu)

    @property
    def menu(self):
        return self._menu


class CodexRequestFileMenu(FileMenu):
    """
    Creates a file menu for the completion request view
    """

    def create(self):
        self._menu.add_command(label="Home",
                               command=self._controller.view.mainWindow)
        endpointMenu = EndpointDropdownMenu(self.menu, self._controller)
        endpointMenu.addCompletion()
        endpointMenu.addEdit()
        endpointMenu = endpointMenu.menu
        self._menu.add_cascade(label="Change endpoint...", menu=endpointMenu)

    @property
    def menu(self):
        return self._menu


class EditMenu(AbstractMenuProduct):
    """
    Abstract product for edit menus
    """


class SettingMenu(AbstractMenuProduct):
    """
    Abstract product for setting menus
    """


class CompletionRequestSettingMenu(SettingMenu):
    """
    Creates a setting menu for the main menu.
    """

    def create(self):
        self._menu.add_command(
            label="Completion Settings",
            command=self._controller.view.completionSettingsWindow
        )

    @property
    def menu(self):
        return self._menu


class EditRequestSettingMenu(SettingMenu):
    """
    Creates a setting menu for the main menu.
    """

    def create(self):
        self._menu.add_command(
            label="Edit Settings",
            command=self._controller.view.editSettingsWindow
        )

    @property
    def menu(self):
        return self._menu


class CodexRequestSettingMenu(SettingMenu):
    """
    Creates a setting menu for the main menu.
    """

    def create(self):
        self._menu.add_command(
            label="Codex Settings",
            command=self._controller.view.codexSettingsWindow
        )

    @property
    def menu(self):
        return self._menu


class HelpMenu(AbstractMenuProduct):
    """
    Abstract product for help menus
    """


if __name__ == "__main__":
    """
    An example of how to create a menu
    """
    root = tk.Tk()
    menu = MainMenu(root, None)
    menu.create()

    root.config(menu=menu.menubar)

    root.mainloop()
