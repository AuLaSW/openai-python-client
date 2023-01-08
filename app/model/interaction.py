import openai
import pprint

# constants
REQUIRED = "required"
OPTIONAL = "optional"

# dictionary of values for request body in Completion API
completionDict = {
    REQUIRED: {
        "model": "text-davinci-003"
    },
    OPTIONAL: {
        "prompt": "",
        # "suffix": NULL,
        "max_tokens": 16,
        "temperature": 0,
        "top_p": 0,
        "n": 1,
        "stream": False,
        # "logprobs": 0,
        "echo": False,
        # "stop": "",
        "presence_penalty": 0,
        "frequency_penalty": 0,
        "best_of": 1,
        # "logit_bias": {},
        "user": ""
    }
}

# dictionary of values for request body in Edit API
editDict = {
    REQUIRED: {
        "model": "text-davinci-edit-001",
        "instruction": ""
    },
    OPTIONAL: {
        "input": "",
        "temperature": 1,
        "top_p": 1,
        "n": 1,
    }
}


# better function for getting all of the necessary keys
# in the dictionaries
def getKeys(dict):
    keys = {
        REQUIRED: [],
        OPTIONAL: []
    }

    for d in dict[REQUIRED]:
        keys[REQUIRED] = d.keys()
        pass

    for d in dict[OPTIONAL]:
        keys[OPTIONAL] = d.keys()
        pass

    return keys


# separate the dictionary into required and optional dicts
def separateDict(dict):
    return dict[REQUIRED], dict[OPTIONAL]


# work with the Completion API for openai
# accepts a dictionary of values
# returns a dictionary of values
def Completion(dict=completionDict):
    required, optional = separateDict(dict)

    response = openai.Completion.create(
            # required inputs
            model=required["model"],

            # optional inputs
            prompt=optional["prompt"],
            # suffix=optional["suffix"],
            max_tokens=optional["max_tokens"],
            temperature=optional["temperature"],
            top_p=optional["top_p"],
            n=optional["n"],
            stream=optional["stream"],
            # logprobs=optional["logprobs"],
            echo=optional["echo"],
            # stop=optional["stop"],
            presence_penalty=optional["presence_penalty"],
            frequency_penalty=optional["frequency_penalty"],
            best_of=optional["best_of"],
            # logit_bias=optional["logit_bias"],
            user=optional["user"]
            )
    return response


# work with the Completion API for openai
# accepts a dictionary of values
# returns a dictionary of values
def Edit(dict=editDict):
    required, optional = separateDict(dict)

    response = openai.Edit.create(
            # required inputs
            model=required["model"],
            instruction=required["instruction"],

            # optional inputs
            input=optional["input"],
            temperature=optional["temperature"],
            top_p=optional["top_p"],
            n=optional["n"],
            )
    return response


if __name__ == "__main__":
    pp = pprint.PrettyPrinter(indent=4)

    print("Running sample Completion Response:")
    pp.pprint(Completion())

    print("Running sample Edit Response:")
    pp.pprint(Edit())
    pass
