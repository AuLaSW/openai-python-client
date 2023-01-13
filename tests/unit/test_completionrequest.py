# test_completionrequest.py
from openaiclient.model.request.completion import CompletionRequest
import unittest


class TestCompletionRequest(unittest.Test):
    def setup(self):
        self.request = CompletionRequest()
        self.REQUIRED_ARGS = 1
    
    # test that the requestDict var is not empty
    # (should be setup)
    def test_RequestNotEmpty(self):
        self.assertTrue(self.request.requestDict)
    
    # test that the requiredArgs var is not empty
    # (should be setup)
    def test_RequiredArgsNotEmpty(self):
        self.assertTrue(self.request.requiredArgs)
    
    # test that the optionalArgs var is not empty
    # (should be setup)
    def test_OptionalArgsNotEmpty(self):
        self.assertTrue(self.request.optionalArgs)
    
    # test that the settings var is not empty
    # (should be setup)
    def test_SettingsNotEmpty(self):
        self.assertTrue(self.request.settings)
    
    # test that the requiredArgs variable and the
    # optionalArgs variable are disjoint
    def test_RequiredOptionalDisjoint(self):
        self.assertTrue(
            self.request.requiredArgs.isdisjoint(
                self.request.optionalArgs
            )
        )
    
    # if the following three tests pass then
    # the optionalArgs variable is also correct.
    
    # test that requiredArgs has the correct
    # number of elements
    def test_RequiredArgsCorrectLength(self):
        self.assertIs(set.len(self.request.requiredArgs), self.REQUIRED_ARGS)
    
    # test that requiredArgs has the correct
    # values
    def test_RequiredArgsCorrectValue(self):
        self.assertIn("model", self.request.requiredArgs)
        
    # # #
    
    # tests that the correct values are in
    # the settings
    def test_SettingsCorrectValue(self):
        self.assertNotIn("prompt", self.request.settings)
    
    # test that the set method rejects a
    # key that is not in the dictionary
    # already
    def test_SetRejectUnknownKey(self):
        key = "testKey"
        value = "testValue"
        
        kwargs = {
            "var": key,
            "val": value
        }
        
        self.assertRaises(
            RuntimeError, 
            self.request.set,
            **kwargs
        )
        


if __name__ == "__main__":
    unittest.mainloop()