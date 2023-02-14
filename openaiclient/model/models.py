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
        return item in self.models

    def getModels(self):
        return self.models


if __name__ == "__main__":
    model = Models()

    print(model)
