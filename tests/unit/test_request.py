# test_request.py
import unittest
from openaiclient.model.request.request import Request


class TestRequest(unittest.TestCase):
    def setUp(self):
        self.request = Request()

    # tests that the requestDict is empty on
    # instantiation
    def test_RequestEmpty(self):
        self.assertFalse(self.request.requestDict)

    # test that requiredArgs is empty
    def test_RequiredArgsEmpty(self):
        self.assertFalse(self.request.requiredArgs)

    # test that optionalArgs is empty
    def test_OptionalArgsEmpty(self):
        self.assertFalse(self.request.optionalArgs)

    # test that settings is empty
    def test_SettingsEmpty(self):
        with self.assertRaises(RuntimeError) as error:
            self.request.settings
        
        self.assertIsInstance(error.exception, RuntimeError) 

    # test that getResponse() returns a NotImplementedError
    def test_GetResponse(self):
        self.assertRaises(NotImplementedError, self.request.getResponse)

    # test that getKeys() called with an empty dictionary
    # will return a runtime error.
    def test_GetKeys(self):
        self.assertRaises(RuntimeError, self.request.getKeys)

    # test that getSettings() called with an empty set
    # will return a runtime error
    def test_getSettings(self):
        self.assertRaises(RuntimeError, self.request.getSettings)

    # test that set() adds key to dictionary
    def test_SetNewKeyError(self):
        kwargs = {
        "var": "testKey",
        "val": "testValue"
        }
        self.assertRaises(RuntimeError, self.request.set, **kwargs)


if __name__ == "__main__":
    unittest.mainloop()
