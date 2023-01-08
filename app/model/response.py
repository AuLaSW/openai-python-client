"""
Class Response:

A class that turns the response JSON from the OpenAI API
into an object that can be used within Python
"""


class Response:
    def __init__(self):
        self.obj = ""
        self.model = ""
        self.text = ""
        self.finish_reason = ""
    pass

    def parseResponse(self, response):
        self.obj = response["object"]
        self.text = response["choices"][0]["text"]
        self.index = response["choices"][0]["index"]

        if "text_completion" in self.obj:
            self.model = response["model"]
            self.finish_reason = response["choices"][0]["finish_reason"]


if __name__ == "__main__":
    pass
