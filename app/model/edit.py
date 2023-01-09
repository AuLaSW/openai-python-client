from model.request import Request
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

    def getResponse(self, dict):
        required, optional = self.separateDict()

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
    req = EditRequest()

    print(req)
