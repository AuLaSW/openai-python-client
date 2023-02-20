"""
SettingsFrame Module
"""
import tkinter as tk
import tkinter.messagebox as messagebox
from openaiclient.view.frame.baseframe import BaseFrame


class SettingsFrame(BaseFrame):
    """
    Class SettingsFrame:

    This class is for a frame that holds settings for
    a user to change. Created to work with the Completion
    and Edit requests to OpenAI.
    """

    def __init__(self, main, controller):
        super().__init__(main, controller)

        # hold the settings we will be using
        self.settings = dict()
        # hold the tk variables for returning inputs from the frame
        self.outputs = dict()

        # row count
        self.row = 0

    # creates all of the widgets for
    # the frame. This default method
    # can be overriden for different
    # types of input in other settings
    # classes.
    def create(self):
        """
        Creates the settings input frames by looping through the settings
        dictionary (self.settings) and creating a SettingsInputFrame object
        for each setting. It then attaches each frame in the next row on
        the frame with the grid() method.

        Finally, it creates the save and exit buttons and attaches them to
        the settings frame (self).
        """
        # key is the label, value is the value in the
        # dictionary of settings
        for key, value in self.settings.items():
            # get the name of the input type
            # str, int, float, or bool
            typeOfValue = type(value).__name__

            try:
                # get the correct setting function
                # based on value type
                func = self.getSettings(typeOfValue)

                # get label and widget from function
                labelWidget, widget = func(key, value)

                # attach label
                labelWidget.grid(
                    column=0,
                    row=self.row,
                    padx=10,
                    pady=10,
                    sticky=tk.E
                )

                # attach widget
                widget.grid(
                    column=1,
                    row=self.row,
                    padx=10,
                    pady=10,
                    sticky=tk.W
                )

                # move down to the next row
                self.row += 1
            except RuntimeError as error:
                # eventually, this needs to be a logger or something
                # similar
                print(error)
                continue

            # potentially better way to implement this?
            # Allows a class to add entries to a
            # settingsDict dictionary, with the keys being
            # the name of the class and the values being
            # the function that that setting type calls
            # to create the correct entry.
            #
            # When a class inherits this class, it can
            # add setting types to the setting dictionary
            # making the settings generation more extensible
            """
            valueTypeName = type(value).__name__
            if valueTypeName is in self.settingsDict.keys():
                self.settingsDict[valueTypeName](key, value)
            else:
                return NotImplementedError()
            """

        self.saveAndExitButtons()

    def getSettings(self, typeOfValue):
        # adjust the frame to match the input type
        match typeOfValue:
            case "str":
                return self.strSetting
            case "int":
                return self.intSetting
            case "float":
                return self.floatSetting
            case "bool":
                return self.boolSetting
            case "Model":
                return self.modelSetting
            case _:
                raise RuntimeError(
                    f"No widget of type {typeOfValue} defined.")

    def saveSettings(self):
        """saves the settings inputted in the window"""
        for key in self.settings:                
            try:
                val = self.outputs[key].get()
                setter = self.setAttr(key)
                setter(self, key, val)

            except KeyError:
                pass
            except tk.TclError as error:
                messagebox.showerror(
                    f"Incorrect input in {key}", f"Key \"{key}\" " + str(error))
    
    def setAttr(self, key):
        """This should be overridden. Returns setter for saveSettings() method"""
        raise NotImplementedError

    def exitSettings(self):
        """exits the window without savings the changes"""
        self.master.destroy()

    def saveAndExitButtons(self):
        """Creates the save and exit button for the frame"""

        frame = tk.Frame(self)

        # button for savings settings
        tk.Button(
            master=frame,
            text="Save",
            command=self.saveSettings
        ).grid(
            column=0,
            row=0,
            padx=10,
            pady=10,
            ipadx=30
        )

        # button to close the window
        tk.Button(
            master=frame,
            text="Exit",
            command=self.exitSettings,
        ).grid(
            column=1,
            row=0,
            padx=10,
            pady=10,
            ipadx=30
        )

        frame.grid(
            column=0,
            row=self.row,
            columnspan=2,
            padx=10,
            pady=10
        )

    # default setting generator. Cleans
    # up the code and makes it easier to
    # define a new setting type
    def baseSetting(
            self,
            tkVar,
            tkFunc,
            key,
            value,
            varKey,
            args=(),
            kwargs={}):
        """
        The function operates as follows:

        1. This function appends the output variable for the setting input
           frame to the kwargs dictionary. The output variable is generated
           by passing tkVar to frame.createOutput().
        2. Then, the function passes tkFunc and kwargs as arguments to
           frame.addSettingWidget(), which returns the labelWidget and the
           widget for inputting data.
        3. The widgets are then placed onto the settings frame with the grid()
           function on the current row.
        """
        args = tuple(args)

        kwargs = kwargs | {varKey: tkVar()}

        # add the output variable to the outputs dictionary
        self.outputs[key] = kwargs[varKey]

        # set value to default value
        kwargs[varKey].set(self.settings[key])

        labelWidget = tk.Label(
            master=self,
            text=key
        )

        # setup the widget that we want.
        # must pass the widget function
        # through the function and pass
        # the kwargs with at least the
        # option tracking variable to
        # track what the entry value
        # is
        widget = tkFunc(
            self,
            *args,
            **kwargs
        )

        return labelWidget, widget

    # string setting input
    def strSetting(self, key, value):
        """
        Creates a string setting input with the Entry object.
        """
        return self.baseSetting(
            tk.StringVar,
            tk.Entry,
            key,
            value,
            "textvariable")

    # integer setting input
    def intSetting(self, key, value):
        """
        Creates an integer setting input with the Entry object.
        """
        return self.baseSetting(
            tk.IntVar,
            tk.Entry,
            key,
            value,
            "textvariable")

    # float setting input
    def floatSetting(self, key, value):
        """
        Creates an integer setting input with the Entry object.
        """
        return self.baseSetting(
            tk.DoubleVar,
            tk.Entry,
            key,
            value,
            "textvariable")

    # boolean setting input
    def boolSetting(self, key, value):
        """
        Creates a boolean setting input with on and off values as 1 and 0 and
        the input as a checkbutton.
        """
        kwargs = dict()
        kwargs["onvalue"] = 1
        kwargs["offvalue"] = 0

        return self.baseSetting(
            tk.IntVar,
            tk.Checkbutton,
            key,
            value,
            "variable",
            kwargs=kwargs
        )

    # float setting input
    def modelSetting(self, key, value):
        """
        Creates a drop-down setting with models as names
        """
        kwargs = {}
        args = set()
        for model in self.controller.models.completionModels.keys():
            args.add(model)
        
        tkVar = tk.StringVar
        tkFunc = tk.OptionMenu
        varKey = "variable"
        
        args = tuple(args)

        kwargs = kwargs | {varKey: tkVar()}

        # add the output variable to the outputs dictionary
        self.outputs[key] = kwargs[varKey]

        # set value to default value
        kwargs[varKey].set(self.settings[key].name)

        labelWidget = tk.Label(
            master=self,
            text=key
        )

        # setup the widget that we want.
        # must pass the widget function
        # through the function and pass
        # the kwargs with at least the
        # option tracking variable to
        # track what the entry value
        # is
        widget = tkFunc(
            self,
            kwargs[varKey],
            *args
        )
        
        return labelWidget, widget


if __name__ == "__main__":
    settingsWindow = tk.Tk()

    settingsFrame = SettingsFrame(
        main=settingsWindow,
        controller=None
    )

    settingsFrame.settings = {
        "testKey": "testVal",
        "testIntKey": 1,
        "testBoolKey": True,
        "testFloatKey": 1.0,
        "testNotInOptions": None
    }

    settingsFrame.create()

    settingsFrame.pack()

    settingsWindow.mainloop()
