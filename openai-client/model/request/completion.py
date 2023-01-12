from openai-client.model.request.request import Request
from openai-client.model.response import Response
import openai

"""
Class CompletionRequest

This is a derived class, with the Request class being the base class.
Handles sending requests to OpenAI for completion.
"""


class CompletionRequest(Request):
    def __init__(self):
        # initialize from parent class Request
        super().__init__()

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
        self.optionalArgs = Set(self.requestDict.keys())
        self.optionalArgs -= self.requiredArgs

        # set of setting arguments
        self.settings = Set(self.requestDict.keys())
        self.settings.remove("prompt")

    def getResponse(self):
        return Response(
                openai.Completion.create(
                    **self.requestDict,
                )
            )

    def addToPrompt(self, input, newLine=False):
        if newLine:
            self.requestDict[self.OPTIONAL]["prompt"] += "\n"
        self.requestDict[self.OPTIONAL]["prompt"] += input


if __name__ == "__main__":
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
