import openai

# get a dictionary of models
models = openai.Model.list()

# print the names of the models that you can use
for model in models["data"]:
    print(model["id"])
    pass
