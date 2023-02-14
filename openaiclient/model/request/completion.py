# import openai
from openaiclient.model.request.request import Request
from openaiclient.model.response import Response

"""
Class CompletionRequest

This is a derived class, with the Request class being the base class.
Handles sending requests to OpenAI for completion.
"""


class CompletionRequest(Request):
    def __init__(self, module):
        # initialize from parent class Request
        super().__init__()

        # set up API class
        self.module = module

        # setup self.requestDict

        self.requestDict = {
            "model": "text-davinci-003",
            "prompt": "",
            "max_tokens": 16,
            "temperature": 0,
            "top_p": 0,
            "n": 1,
            "stream": False,
            "echo": False,
            "presence_penalty": 0,
            "frequency_penalty": 0,
            "best_of": 1,
            "user": ""
            # these keys I cannot get to work and are optional,
            # so they are commented out until they work
            #
            # "suffix": NULL,
            # "logprobs": 0,
            # "stop": "",
            # "logit_bias": {},
        }

        # required values
        self.requiredArgs = {
            "model",
        }

        # optional values
        self.optionalArgs = set(self.requestDict.keys())
        self.optionalArgs -= self.requiredArgs

        # set of setting arguments
        self.settings = set(self.requestDict.keys())
        self.settings.remove("prompt")

    def getResponse(self):
        return Response(
            self.module.Completion.create(
                **self.requestDict,
            )
        )

    def addToPrompt(self, newInput, newLine=False):
        if len(self.requestDict["prompt"]) == 0:
            self.set("prompt", newInput)
        elif newLine:
            self.requestDict["prompt"] += "\n"
        else:
            self.requestDict["prompt"] += " " + newInput


if __name__ == "__main__":
    pass
"""
    req = CompletionRequest()
    req.setPrompt("Tell me a joke")
    req.setEcho(True)

    # print(req)

    response = req.getResponse()

    print("\nPrompt One:\n")
    print(response.getText())

    req.setPrompt(response.getText())
    req.addToPrompt("I don't know. What?", True)

    response = req.getResponse()

    print("\nPrompt Two:\n")
    print(response.getText())
"""
