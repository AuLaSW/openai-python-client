"""
Class Response:

A class that turns the response JSON from the OpenAI API
into an object that can be used within Python
"""


class Response:
    def __init__(self, response):
        self.obj = response["object"]
        self.text = response["choices"][0]["text"]
        self.index = response["choices"][0]["index"]

        if "text_completion" in self.obj:
            self.model = response["model"]
            self.finish_reason = response["choices"][0]["finish_reason"]

    def getText(self):
        return self.text

    def getFinishReason(self):
        try:
            return self.finish_reason
        except AttributeError:
            raise RuntimeError


if __name__ == "__main__":
    pass
