import openai


# retreives the different GPT models
# from OpenAI and creates a list with
# all of the valid IDs
def getModels():
    # constant values
    TEXT_KEY = "text"
    ID_KEY = "id"
    DATA_KEY = "data"
    DELIM = "-"

    # list of text models
    models = []

    # print the names of the models that you can use
    for model in openai.Model.list()[DATA_KEY]:
        if model[ID_KEY].startswith(TEXT_KEY) > 0:
            if len(model[ID_KEY].split(DELIM)) == 3:
                models.append(model["id"])
                pass
            pass
        pass
    return models


# generate list of text models
textModels = getModels()
