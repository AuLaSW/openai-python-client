from openai-client.model.request.request import Request
from openai-client.model.response import Response
import openai

"""
Class EditRequest

This is a derived class, with the Request class being the base class.
Handles sending requests to OpenAI for completion.
"""


class EditRequest(Request):
    def __init__(self):
        # initialize from parent class Request
        super().__init__()

        # setup self.requestDict

        # required values
        self.requestDict[self.REQUIRED] = {
            "model": "text-davinci-edit-001",
            "instruction": ""
        }

        # optional values
        self.requestDict[self.OPTIONAL] = {
            "input": "",
            "temperature": 1,
            "top_p": 1,
            "n": 1,
        }
        
        self.notSettings = [ "instruction", "input" ]

    def getResponse(self):
        return Response(
                openai.Edit.create(
                    # required inputs
                    model=self.getModel(),
                    instruction=self.getInstruction(),

                    # optional inputs
                    input=self.getInput(),
                    temperature=self.getTemperature(),
                    top_p=self.getTopP(),
                    n=self.getN(),
                )

    def getModel(self):
        return self.requestDict[self.REQUIRED]["model"]

    def setModel(self, input):
        self.requestDict[self.REQUIRED]["model"] = input
        
    def getInstruction(self):
        return self.requestDict[self.REQUIRED]["instruction"]

    def setInstruction(self, input):
        self.requestDict[self.REQUIRED]["instruction"] = input

    def getInput(self):
        return self.requestDict[self.OPTIONAL]["input"]

    def setInput(self, input):
        self.requestDict[self.OPTIONAL]["input"] = input
 
    def getTemperature(self):
        return self.requestDict[self.OPTIONAL]["temperature"]

    def setTemperature(self, input):
        self.requestDict[self.OPTIONAL]["temperature"] = input       

    def getTopP(self):
        return self.requestDict[self.OPTIONAL]["top_p"]

    def setTopP(self, input):
        self.requestDict[self.OPTIONAL]["top_p"] = input

    def getN(self):
        return self.requestDict[self.OPTIONAL]["n"]

    def setN(self, input):
        self.requestDict[self.OPTIONAL]["n"] = input


if __name__ == "__main__":
    req = EditRequest()

    print(req)
