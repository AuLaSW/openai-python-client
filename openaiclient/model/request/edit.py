from openaiclient.model.request.request import Request
from openaiclient.model.response import Response
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
        self.requestDict = {
            "model": "text-davinci-edit-001",
            "instruction": ""
            "input": "",
            "temperature": 1,
            "top_p": 1,
            "n": 1,
        }

        # required arguments
        self.requiredArgs = {
            "model",
            "instruction",
        }

        # optional arguments
        self.optionalArgs = Set(self.requestDict.keys())
        self.optionalArgs -= self.requiredArgs

        # arguments that are settings
        self.settings = Set(self.requestDict.keys())
        self.settings.remove("instruction")
        self.settings.remove("input")

    def getResponse(self):
        return Response(
                openai.Edit.create(
                    **self.requestDict,
                )


if __name__ == "__main__":
    req=EditRequest()

    print(req)
