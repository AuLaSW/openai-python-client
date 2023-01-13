# test_response.py
from openai.model.response import Response
import unittest


class TestResponse(unittest.TestCase):
    def test_getText(self):
        result = self.response.getText()
        reference = self.dictionary["choices"][0]["text"]

        self.assertEqual(result, reference)

    def test_getFinishReason(self):
        result = self.response.getFinishReason()
        reference = self.dictionary["choices"][0]["finish_reason"]

        self.assertEqual(result, reference)


class TestResponseTextCompletion(TestResponse):
    def setUp(self):
        self.dictionary = {
            "object": "text_completion",
            "choices": [ {
                "text": "input text"
                "index": 0
                "finish_reason": "finished"
                }
            ],
            "model": "text-davinci-003"
        }

        self.response = Response(self.dictionary)


class TestResponseEdit(TestResponse):
    def setUp(self):
        self.dictionary = {
            "object": "edit",
            "choices": [ {
                "text": "input text"
                "index": 0
                }
            ],
        }

        self.response = Response(self.dictionary)


if __name__ == "__main__":
    unittest.main()