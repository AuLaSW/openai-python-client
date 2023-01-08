import openai


# sort the textModels into a more
# friendly list.
def sortModels(modelList):
    return modelList


# retreives the different GPT models
# from OpenAI and creates a list with
# all of the valid IDs
def getModels():
    # constant values
    TEXT_KEY = "text"
    ID_KEY = "id"
    DATA_KEY = "data"

    # list of text models
    models = []

    # print the names of the models that you can use
    for model in openai.Model.list()[DATA_KEY]:
        if model[ID_KEY].startswith(TEXT_KEY) > 0:
            models.append(model["id"])
            pass
        pass
    return sortModels(models)


# generate list of text models
textModels = getModels()

if __name__ == "__main__":
    print(textModels)
    pass
