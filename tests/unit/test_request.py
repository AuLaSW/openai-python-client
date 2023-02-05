# test_request.py
import unittest
from openaiclient.model.request.request import Request


class TestRequest(unittest.TestCase):
    def setup(self):
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
        self.assertFalse(self.request.settings)

    # test that getResponse() returns a NotImplementedError
    def test_GetResponse(self):
        self.assertRaises(NotImplementedError, self.request.getResponse)

    # test that getKeys() called with an empty dictionary
    # will return a runtime error.
    def test_GetKeys(self):
        self.assertRaise(RuntimeError, self.request.getKeys)

    # test that getSettings() called with an empty set
    # will return a runtime error
    def test_getSettings(self):
        self.assertRaise(RuntimeError, self.request.getSettings)

    # test that set() sets the correct value
    # also tests that get() works
    def test_SetCorrectValue(self):
        key = "testKey"
        value = "testValue"
        self.request.set(key, value)

        self.assertEquals(self.request.get(key), value)

    # test that set() adds key to dictionary
    def test_SetCorrectKey(self):
        key = "testKey"
        value = "testValue"
        self.request.set(key, value)

        self.assertIn(key, self.request.getKeys())


if __name__ == "__main__":
    unittest.mainloop()
