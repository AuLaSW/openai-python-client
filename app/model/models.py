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
            self.COMPLETION: [],
            self.EDIT: []
        }

        # populate the model dictionary
        self.generateModels()

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

    # returns a dictionary of usable text models
    def generateModels(self):
        # loop through the list of models
        for model in openai.Model.list()["data"]:
            # only focus on the id of the model
            modelID = model["id"]

            # is the model a text model
            textModel = "text" in modelID

            # is the model not a search or code model?
            # I'm not sure what the : is used for in the model
            # names, but I don't want to use those
            codeModel = "code" in modelID
            searchModel = "search" in modelID
            simModel = "similarity" in modelID
            insModel = "insert" in modelID
            embModel = "embedding" in modelID
            colModel = ":" in modelID
            validModel = (not codeModel and not searchModel
                          and not simModel and not colModel
                          and not insModel and not embModel)

            # is the model an edit model?
            editModel = "edit" in modelID

            if textModel and validModel:
                if editModel:
                    self.models[self.EDIT].append(modelID)
                else:
                    self.models[self.COMPLETION].append(modelID)

    def getModels(self):
        return self.models


if __name__ == "__main__":
    model = Models()

    print(model)
