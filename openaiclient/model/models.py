import openai

"""
Class Models

This class retrieves the models from the OpenAI API
and creates a dictionary of the usable classes.
"""


class Models:
    def __init__(self):
        self.COMPLETION = "Completion"
        self.EDIT = "Edit"
        
        # dictionary of models
        self.models = {
            self.COMPLETION: [
                "text-davinci-003",
                "text-curie-001",
                "text-babbage-001",
                "text-ada-001"
            ],
            self.EDIT: [
                "text-davinci-edit-001"
            ]
        }

    def __str__(self):
        strModels = "Usable Models:\n"

        strModels += "  " + self.COMPLETION + " Models:\n"

        for key in self.models[self.COMPLETION]:
            strModels += "    " + key + "\n"

        strModels += "  " + self.EDIT + " Models:\n"

        for key in self.models[self.EDIT]:
            strModels += "    " + key + "\n"

        return strModels

    def __contains__(self, item):
        return item in self.models[self.COMPLETION] + self.models[self.EDIT]

    def getModels(self):
        return self.models


class Model:
    def __init__(self, name, max_tokens, type):
        self._name = name
        self._max_tokens = max_tokens
        self._type = type
    
    @property
    def model(self):
        return self._name
    
    @property
    def max_tokens(self):
        return self._max_tokens
        
    @property
    def type(self):
        return self._type


if __name__ == "__main__":
    model = Models()

    print(model)
