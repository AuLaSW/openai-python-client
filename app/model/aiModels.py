import openai


def getModels():
    # constant values
    TEXT_KEY = "text"
    ID_KEY = "id"
    DATA_KEY = "data"

    # list of text models
    textModels = []

    # print the names of the models that you can use
    for model in openai.Model.list()[DATA_KEY]:
        if model[ID_KEY].startswith(TEXT_KEY) > 0:
            if len(model[ID_KEY].split("-")) == 3:
                textModels.append(model["id"])
                pass
            pass
        pass
    return textModels
