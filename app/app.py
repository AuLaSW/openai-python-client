import openai

# get API key from usr folder
openai.api_key = "API_KEY"

# get a dictionary of models
models = openai.Model.list()

# print the names of the models that you can use
for model in models["data"]:
    print(model["id"])
    pass
