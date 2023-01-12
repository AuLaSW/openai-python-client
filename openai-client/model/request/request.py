"""
Class Request:

An abstract class used to model different request types to the
OpenAI API.
"""


class Request:
    def __init__(self):
        # dictionary of request arguments
        self.requestDict = dict()

        # set of required request arguments
        self.requiredArgs = {}
        
        # set of optional request arguments
        self.optionalArgs = {}

        # set of request settings
        self.settings = {}

    def __str__(self):
        # this produces a header for the output that contains the
        # class name (works with sublcasses, too)
        strRequest = self.__class__.__name__ + " Input:\n"

        # required dictionary and optional dictionary separation
        requiredDict, optionalDict = self.separateDict()

        # add required entries to the string
        strRequest += "  Required Entries:\n"

        for key in requiredDict:
            strRequest += "    " + key + ": " + str(requiredDict[key]) + "\n"

        # add optional entries to the string
        strRequest += "  Optional Entries:\n"

        for key in optionalDict:
            strRequest += "    " + key + ": " + str(optionalDict[key]) + "\n"

        return strRequest

    def getResponse(self):
        return NotImplementedError()

    # returns required keys and optional keys, in that order
    def getKeys(self):
        return self.requestDict.keys()

    # returns dict of settings
    def getSettings(self):
        return self.settings

    def get(self, option, var):
        return self.requestDict[var]
    
    def set(self, option, var, val):
        self.requestDict[var] = val