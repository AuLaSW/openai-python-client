# test_response.py
from openai.model.response import Response
import unittest


class TestResponse(unittest.TestCase):
    def test_correctObject(self):
        self.assertEqual(self.obj, response["object"])
        
    def test_correctText(self):
        self.assertEqual(self.text, response["choices"][0]["text"])
    
    def test_correctIndex(self):
        self.assertEqual(self.index, response["choices"][0]["index"])

    # test that getText() returns the 
    # text object
    def test_getText(self):
        result = self.response.getText()
        reference = self.dictionary["choices"][0]["text"]

        self.assertEqual(result, reference)

    # test that getFinishReason() returns
    # the finish reason
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
    
    def test_correctModel(self):
        self.assertEqual(self.model, response["model"])
            
    
    def test_correctFinishReason(self):
        self.assertEqual(
                self.finish_reason, 
                response["choices"][0]["finish_reason"]
            )


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