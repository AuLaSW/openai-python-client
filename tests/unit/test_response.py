# test_response.py
import unittest
from openaiclient.model.response import Response


class TestResponseWrapper:
    class TestResponse(unittest.TestCase):
        def test_CorrectObject(self):
            self.assertEqual(
                self.response.obj,
                self.dictionary["object"])

        def test_CorrectText(self):
            self.assertEqual(
                self.response.text,
                self.dictionary["choices"][0]["text"])

        def test_CorrectIndex(self):
            self.assertEqual(
                self.response.index,
                self.dictionary["choices"][0]["index"])

        # test that getText() returns the
        # text object
        def test_GetText(self):
            result = self.response.getText()
            reference = self.dictionary["choices"][0]["text"]

            self.assertEqual(result, reference)


class TestResponseTextCompletion(TestResponseWrapper.TestResponse):
    def setUp(self):
        self.dictionary = {
            "object": "text_completion",
            "choices": [{
                "text": "input text",
                "index": 0,
                "finish_reason": "finished"
            }
            ],
            "model": "text-davinci-003"
        }

        self.response = Response(self.dictionary)

    def test_CorrectModel(self):
        self.assertEqual(
            self.response.model,
            self.dictionary["model"])

    def test_CorrectFinishReason(self):
        self.assertEqual(
            self.response.finish_reason,
            self.dictionary["choices"][0]["finish_reason"]
        )

    # test that getFinishReason() returns
    # the finish reason
    def test_GetFinishReason(self):
        result = self.response.getFinishReason()
        reference = self.dictionary["choices"][0]["finish_reason"]

        self.assertEqual(result, reference)


class TestResponseEdit(TestResponseWrapper.TestResponse):
    def setUp(self):
        self.dictionary = {
            "object": "edit",
            "choices": [{
                "text": "input text",
                "index": 0,
            }
            ],
        }

        self.response = Response(self.dictionary)

    def test_GetFinishReasonException(self):
        self.assertRaises(RuntimeError, self.response.getFinishReason)


if __name__ == "__main__":
    unittest.main()
