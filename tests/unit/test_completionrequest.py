"""
This module tests the CompletionRequest class.
"""
import unittest
from tests.unit.fixture import api
from openaiclient.model.request.completion import CompletionRequest
from openaiclient.model.response import Response


class TestCompletionRequest(unittest.TestCase):
    """
    This class holds the test functions for the CompletionRequest class.

    setUp():
        Setup request and REQUIRED_ARGS before all of the tests.

    test_RequestNotEmpty():
        Tests that the requestDict is not empty. There should be a default
        requestDict() created.

    test_RequiredArgsNotEmpty():
        Tests that requiredArgs is not empty. There are required arguments.

    test_OptionalArgsNotEmpty():
        Tests that optionalArgs is not emtpy. There are optional arguments.

    test_SettingsNotEmpty():
        Tests that the settings are not emtpy.

    test_RequiredOptionalDisjoint():
        Tests that requiredArgs and OptionalArgs are disjoint. There are no
        arguments that are both required and optional.

    test_RequiredArgsCorrectLength():
        Tests that the requiredArgs variable has the correct number of required
        arguments.

    test_RequiredArgsCorrectValue():
        Tests that the requiredArgs variable has the correct values.

    test_SettingsCorrectValue():
        Tests that the settings variable has the correct values.

    test_SetRejectUnknownKey():
        Tests that the Set() function rejects a key that is not already in the
        dictionary.



    Implicit Tests:
    ---------------
        
        If test_RequiredOptionalDisjoint(), test_RequiredArgsCorrectLength(),
        and test_RequiredArgsCorrectValue() all pass, then the optionalArgs
        variable would also pass the same tests. This is because the two sets
        are disjoint and contain different values, so if requiredArgs contains
        the correct values and is disjoint from optionalArgs, then optionalArgs
        must contain the correct values too.
    """
    def setUp(self):
        self.request = CompletionRequest(api)
        self.REQUIRED_ARGS = 1


class TestFunctions(TestCompletionRequest):
    """
    This class holds the functional tests for the Completion class.
    
    test_GetResponse():
        Tests that the getResponse() method returns a Response object.
    
    test_AddToPrompt():
        Adds a prompt to an empty prompt and tests that the function
        completes successfully.
    
    test_AddToOriginalPrompt():
        Adds a prompt to an original prompt without making a new line.
        Tests that the function completes successfully.
    
    test_AddNewLineToOriginalPrompt():
        Adds a prompt to an original prompt while also generating a new
        line. Tests that the function completes successfully.
    """
    def test_GetResponse(self):
        """
        Asserts that the object returned by getResponse() is a Response object.
        """
        self.assertIsInstance(self.request.getResponse(), Response)
    
    def test_addToPrompt(self):
        additionalPrompt = "Add this to the prompt."
        
        self.request.addToPrompt(additionalPrompt)
        
        self.assertEqual(self.request.requestDict["prompt"], additionalPrompt)

    def test_AddToOriginalPrompt(self):
        originalPrompt = "This is the first prompt."
        additionalPrompt = "Add this to the prompt."
        
        self.request.prompt = originalPrompt
        
        self.request.addToPrompt(additionalPrompt)
        
        self.assertEqual(
            self.request.requestDict["prompt"], 
            originalPrompt + " " + additionalPrompt
        )
    
    def test_AddNewLineToOriginalPrompt(self):
        originalPrompt = "This is the first prompt."
        additionalPrompt = "Add this to the prompt."
        
        self.request.prompt = originalPrompt
        
        self.request.addToPrompt(additionalPrompt, True)
        
        self.assertEqual(
            self.request.requestDict["prompt"], 
            originalPrompt + "\n" + additionalPrompt
        )


class TestSettings(TestCompletionRequest):
    def test_RequestNotEmpty(self):
        """
        Asserts that requestDict is not empty.
        """
        self.assertTrue(self.request.requestDict)

    def test_RequiredArgsNotEmpty(self):
        """
        Asserts that requiredArgs is not empty.
        """
        self.assertTrue(self.request.requiredArgs)

    def test_OptionalArgsNotEmpty(self):
        """
        Asserts that optionalArgs is not empty.
        """
        self.assertTrue(self.request.optionalArgs)

    def test_SettingsNotEmpty(self):
        """
        Asserts that optionalArgs is not empty.
        """
        self.assertTrue(self.request.settings)

    def test_RequiredOptionalDisjoint(self):
        """
        Asserts that requiredArgs and optionalArgs are disjoint.
        """
        self.assertTrue(
            self.request.requiredArgs.isdisjoint(
                self.request.optionalArgs
            )
        )

    def test_RequiredArgsCorrectLength(self):
        """
        Asserts that requiredArgs has the correct number of arguments.
        """
        self.assertIs(len(self.request.requiredArgs), self.REQUIRED_ARGS)

    def test_RequiredArgsCorrectValue(self):
        """
        Asserts that requiredArgs has the correct arguments.
        """
        self.assertIn("model", self.request.requiredArgs)

    def test_SettingsCorrectValue(self):
        """
        Asserts that "prompt" is not in settings.
        """
        self.assertNotIn("prompt", self.request.settings)


if __name__ == "__main__":
    unittest.mainloop()
