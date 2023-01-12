from model.request.request import Request
from model.response import Response
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

        # required values
        self.requestDict[self.REQUIRED] = {
            "model": "text-davinci-003"
        }

        # optional values
        self.requestDict[self.OPTIONAL] = {
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

        self.notSettings = [ "prompt" ]

    def getResponse(self):
        return Response(
                openai.Completion.create(
                    # required inputs
                    model=self.getModel(),

                    # optional inputs
                    prompt=self.getPrompt(),
                    max_tokens=self.getMaxTokens(),
                    temperature=self.getTemperature(),
                    top_p=self.getTopP(),
                    n=self.getN(),
                    stream=self.getStream(),
                    echo=self.getEcho(),
                    presence_penalty=self.getPresencePenalty(),
                    frequency_penalty=self.getFrequencyPenalty(),
                    best_of=self.getBestOf(),
                    user=self.getUser()
                    # suffix=optional["suffix"],
                    # logprobs=optional["logprobs"],
                    # stop=optional["stop"],
                    # logit_bias=optional["logit_bias"],
                )
            )
        """
        Another option could look like this:

        required = self.requestDict[self.REQUIRED]
        optional = self.requestDict[self.OPTIONAL]

        return Response(
                Comp.create(
                    required | optional
                )
            )
        """

    def getSettings(self):
        allKeys, optionalKeys = self.getKeys()
        
        allKeys.extend(optionalKeys)
        
        for key in allKeys:
            if key is in self.notSettings:
                allKeys.remove(key)

        return allKeys

    def getModel(self):
        return self.get(self.REQUIRED, "model")

    def setModel(self, input):
        self.set(self.REQUIRED, "model", input)

    def getPrompt(self):
        return self.get(self.OPTIONAL, "prompt")

    def setPrompt(self, input):
        self.set(self.OPTIONAL, "prompt", input) 

    def addToPrompt(self, input, newLine=False):
        if newLine:
            self.requestDict[self.OPTIONAL]["prompt"] += "\n"
        self.requestDict[self.OPTIONAL]["prompt"] += input

    def getMaxTokens(self):
        return self.get(self.OPTIONAL, "max_tokens")

    def setMaxTokens(self, input):
        self.set(self.OPTIONAL, "max_tokens", input) 

    def getTemperature(self):
        return self.get(self.OPTIONAL, "temperature")

    def setTemperature(self, input):
        self.set(self.OPTIONAL, "temperature", input) 

    def getTopP(self):
        return self.get(self.OPTIONAL, "top_p")

    def setTopP(self, input):
        self.set(self.OPTIONAL, "top_p", input) 

    def getN(self):
        return self.get(self.OPTIONAL, "n")

    def setN(self, input):
        self.set(self.OPTIONAL, "n", input) 

    def getStream(self):
        return self.get(self.OPTIONAL, "stream")

    def setStream(self, input):
        self.set(self.OPTIONAL, "stream", input) 

    def getEcho(self):
        return self.get(self.OPTIONAL, "echo")

    def setEcho(self, input):
        self.set(self.OPTIONAL, "echo", input) 

    def getPresencePenalty(self):
        return self.get(self.OPTIONAL, "presence_penalty")

    def setPresencePenalty(self, input):
        self.set(self.OPTIONAL, "presence_penalty", input) 

    def getFrequencyPenalty(self):
        return self.get(self.OPTIONAL, "frequency_penalty")

    def setFrequencyPenalty(self, input):
        self.set(self.OPTIONAL, "frequency_penalty", input) 

    def getBestOf(self):
        return self.get(self.OPTIONAL, "best_of")

    def setBestOf(self, input):
        self.set(self.OPTIONAL, "best_of", input) 

    def getUser(self):
        return self.get(self.OPTIONAL, "user")

    def setUser(self, input):
        self.set(self.OPTIONAL, "user", input) 


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
