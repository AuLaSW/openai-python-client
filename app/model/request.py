"""
Class Request:

An abstract class used to model different request types to the
OpenAI API.
"""


class Request:
    def __init__(self):
        self.REQUIRED = "required"
        self.OPTIONAL = "optional"

        self.requestDict = {
            self.REQUIRED: {},
            self.OPTIONAL: {}
        }

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

    def getResponse(self, dict):
        return NotImplementedError()

    # returns required keys and optional keys, in that order
    def getKeys(self):
        keys = {
            self.REQUIRED: [],
            self.OPTIONAL: []
        }

        for d in self.requestDict[self.REQUIRED]:
            keys[self.REQUIRED] = d.keys()

        for d in self.requestDict[self.OPTIONAL]:
            keys[self.OPTIONAL] = d.keys()

        return keys[self.REQUIRED], keys[self.OPTIONAL]

    # separate the dictionary into a required dictionary and
    # an optional dictionary
    def separateDict(self):
        return self.requestDict[self.REQUIRED], self.requestDict[self.OPTIONAL]
