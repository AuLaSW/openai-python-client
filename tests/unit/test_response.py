# test_response.py
import unittest

from app.model.response import Response


class TestResponse(unittest.TestCase):
    def setUp(self):
        self.dictionary = {
            "object": "object value",
            "choices": [ {
                "text": "input text"
                "index": 0
                "finish_reason": "finished"
                }
            ],
            "model": "model value"
        }

        self.response = Response(self.dictionary)

    def test_getText(self):
        result = self.response.getText()
        reference = self.dictionary["choices"][0]["text"]

        self.assertEqual(result, reference)

    def test_getFinishReason(self):
        result = self.response.getFinishReason()
        reference = self.dictionary["choices"][0]["finish_reason"]

        self.assertEqual(result, reference)

if __name__ == "__main__":
    pass