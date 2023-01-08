import openai


def getModels():
    # constant values
    TEXT_KEY = "text"
    EDIT_KEY = "edit"
    ID_KEY = "id"
    DATA_KEY = "data"

    # list of text models
    textModels = dict()

    # set up keys for the text models
    textModels[TEXT_KEY] = []
    textModels[EDIT_KEY] = []

    # print the names of the models that you can use
    for model in openai.Model.list()[DATA_KEY]:
        if model[ID_KEY].count(TEXT_KEY) > 0:
            if model[ID_KEY].count(EDIT_KEY) > 0:
                textModels[EDIT_KEY].append(model[ID_KEY])
                pass
            else:
                textModels[TEXT_KEY].append(model[ID_KEY])
                pass
            pass
        pass
    return textModels
