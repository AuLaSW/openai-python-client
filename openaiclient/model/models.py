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
        self._models = {
            "text-davinci-003": Model(
                "text-davinci-003",
                4_000,
                self.COMPLETION
            ),
            "text-curie-001": Model(
                "text-curie-001",
                2_048,
                self.COMPLETION
            ),
            "text-babbage-001": Model(
                "text-babbage-001",
                2_048,
                self.COMPLETION
            ),
            "text-ada-001": Model(
                "text-ada-001",
                2_048,
                self.COMPLETION
            ),
            "text-davinci-edit-001": Model(
                "text-davinci-edit-001",
                2_048,
                self.EDIT
            ),
        }

    def __str__(self):
        strModels = "Usable Models:\n"

        strModels += "  " + self.COMPLETION + " Models:\n"

        for _, model in self.models.items():
            if model.type == self.COMPLETION:
                strModels += "    " + model.model + "\n"

        strModels += "  " + self.EDIT + " Models:\n"

        for _, model in self.models.items():
            if model.type == self.EDIT:
                strModels += "    " + model.model + "\n"

        return strModels

    def __contains__(self, item):
        return item in self._models

    @property
    def models(self):
        return self._models


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
