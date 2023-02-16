"""
This module tests the CompletionRequest class.
"""
import unittest
from tests.unit.fixture import api
from openaiclient.model.models import Models
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
        models = Models()
        self.request = CompletionRequest(api, models)
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
    
    def test_AddToPrompt(self):
        additionalPrompt = "Add this to the prompt."
        
        self.request.addToPrompt(additionalPrompt)
        
        self.assertEqual(self.request.prompt, additionalPrompt)

    def test_AddToOriginalPrompt(self):
        originalPrompt = "This is the first prompt."
        additionalPrompt = "Add this to the prompt."
        
        self.request.prompt = originalPrompt
        
        self.request.addToPrompt(additionalPrompt)
        
        self.assertEqual(
            self.request.prompt, 
            originalPrompt + " " + additionalPrompt
        )
    
    def test_AddNewLineToOriginalPrompt(self):
        originalPrompt = "This is the first prompt."
        additionalPrompt = "Add this to the prompt."
        
        self.request.prompt = originalPrompt
        
        self.request.addToPrompt(additionalPrompt, True)
        
        self.assertEqual(
            self.request.prompt, 
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

class TestProperties(TestCompletionRequest):
    def test_ModelSetter(self):
        """
        Asserts that adding a valid model results in the model
        value being correctly updated
        """
        model = "text-davinci-003"
        self.request.setModel(model)
        
        self.assertEqual(self.request.model, model)

    def test_ModelSetterInvalidModel(self):
        """
        Asserts that an error is thrown when an invalid model is
        inputted into the setter.
        """
        model = "test-model"
        
        with self.assertRaises(RuntimeError) as error:
            self.request.model = model
        
        self.assertIsInstance(error.exception, RuntimeError)
        
    def test_ModelSetterIntegerInput(self):
        """
        Asserts that an error is thrown when an integer is inputted
        into the model setter
        """
        for model in range(-10, 10, 1):
            with self.subTest(model=model):
                with self.assertRaises(RuntimeError) as error:
                    self.request.model = model
                
                self.assertIsInstance(error.exception, RuntimeError)
    
    def test_Prompt(self):
        """
        Asserts that when a string is passed into the prompt setter,
        the prompt is correctly changed.
        """
        prompt = "this is a test"
        self.request.prompt = prompt
        
        self.assertEqual(self.request.prompt, prompt)

    def test_PromptIntegerFail(self):
        """
        Asserts that when a number is passed into the prompt, it
        throws an error.
        """
        for prompt in range(-10, 10, 1):
            with self.subTest(prompt=prompt):
                with self.assertRaises(RuntimeError) as error:
                    self.request.prompt = prompt
                
                self.assertIsInstance(error.exception, RuntimeError)
    
    def test_PromptFloatFail(self):
        """
        Asserts that when a number is passed into the prompt, it
        throws an error.
        """
        for prompt in [-1.0, -0.5, 0.0, 0.5, 1.0]:
            with self.subTest(prompt=prompt):
                with self.assertRaises(RuntimeError) as error:
                    self.request.prompt = prompt
                
                self.assertIsInstance(error.exception, RuntimeError)
    
    def test_PromptBooleanFail(self):
        """
        Asserts that when a boolean is passed into the prompt,
        it throws an error.
        """
        for prompt in [True, False]:
            with self.subTest(prompt=prompt):
                with self.assertRaises(RuntimeError) as error:
                    self.request.prompt = prompt
                
                self.assertIsInstance(error.exception, RuntimeError)
    
    def test_Max_Tokens(self):
        """
        Asserts that when a valid integer is passed that the correct value is modified
        """
        for model in self.request.models.completionModels:
            with self.subTest(model=model):
                for max_tokens in range(1, model.max_tokens + 1, 32):
                    with self.subTest(max_tokens=max_tokens):
                        self.request.max_tokens = max_tokens
                        
                        self.assertEqual(self.request.max_tokens, max_tokens)
    
    def test_Max_TokensFloatError(self):
        """
        Asserts that when a float is passed to max_tokens an error is thrown.
        """
        for max_tokens in range(1, 100):
            max_tokens = 0.5 * float(max_tokens)
            with self.subTest(max_tokens=max_tokens):
                with self.assertRaises(RuntimeError) as error:
                    self.request.max_tokens = max_tokens
                
                self.assertIsInstance(error.exception, RuntimeError)
    
    def test_Max_TokensBooleanError(self):
        """
        Asserts that when a boolean is passed to max_tokens an error is thrown.
        """
        for max_tokens in [True, False]:
            with self.subTest(max_tokens=max_tokens):
                with self.assertRaises(RuntimeError) as error:
                    self.request.max_tokens = max_tokens
                
                self.assertIsInstance(error.exception, RuntimeError)
    
    def test_Max_TokensLessThanZero(self):
        """
        Asserts that when an integer less than or equal to zero is passed an error is thrown.
        """
        for max_tokens in range(-10, 0):
            with self.subTest(max_tokens=max_tokens):
                with self.assertRaises(RuntimeError) as error:
                    self.request.max_tokens = max_tokens
                    
                self.assertIsInstance(error.exception, RuntimeError)
    
    def test_Max_TokensGreaterThanMaximum(self):
        """
        Asserts that when an integer greater than the maximum number of tokens is passed an error is thrown.
        """
        for _, model in self.request.models.models.items():
            with self.subTest(model=model):
                for i in range(1, 20):
                    with self.subTest(i=i):
                        self.request.model = model.name
                        with self.assertRaises(RuntimeError) as error:
                            self.request.max_tokens = model.max_tokens + i
                            
                        self.assertIsInstance(error.exception, RuntimeError)
    
    def test_Temperature(self):
        """
        Assert that a correct input to temperature parameter will change correct data field.
        """
        for temperature in range(0, 20, 1):
            temperature *= 0.1
            with self.subTest(temperature=temperature):
                self.request.temperature = temperature
                self.assertEqual(self.request.temperature, temperature)
                
    def test_TemperatureIntegerError(self):
        """
        Asserts that when an integer is passed to temperature an error is thrown.
        """
        for temperature in range(-10, 10):
            with self.subTest(temperature=temperature):
                with self.assertRaises(RuntimeError) as error:
                    self.request.temperature = temperature
                
                self.assertIsInstance(error.exception, RuntimeError)
    
    def test_TemperatureBooleanError(self):
        """
        Asserts that when a boolean is passed to temperature an error is thrown.
        """
        for temperature in [True, False]:
            with self.subTest(temperature=temperature):
                with self.assertRaises(RuntimeError) as error:
                    self.request.temperature = temperature
                
                self.assertIsInstance(error.exception, RuntimeError)
    
    def test_TemperatureLessThanZero(self):
        """
        Asserts that when an float less than or equal to zero is passed an error is thrown.
        """
        for temperature in range(-10, 0):
            temperature *= 0.1
            with self.subTest(temperature=temperature):
                with self.assertRaises(RuntimeError) as error:
                    self.request.temperature = temperature
                    
                self.assertIsInstance(error.exception, RuntimeError)
    
    def test_TemperatureGreaterThanMaximum(self):
        """
        Asserts that when a float greater than the maximum temperature is passed an error is thrown.
        """
        for temperature in range(30, 50):
            temperature *= 0.1
            with self.subTest(temperature=temperature):
                with self.assertRaises(RuntimeError) as error:
                    self.request.temperature = temperature
                    
                self.assertIsInstance(error.exception, RuntimeError)

    def test_Top_P(self):
        """
        Asserts that when a valid input in made it changes the correct value.
        """
        for top_p in range(0,10):
            top_p *= 0.1
            with self.subTest(top_p=top_p):
                self.request.top_p = top_p
                self.assertEqual(self.request.top_p, top_p)
    
    def test_Top_PIntegerError(self):
        """
        Asserts that when an integer is passed to top_p an error is thrown.
        """
        for top_p in range(-10, 10):
            with self.subTest(top_p=top_p):
                with self.assertRaises(RuntimeError) as error:
                    self.request.top_p = top_p
                
                self.assertIsInstance(error.exception, RuntimeError)
    
    def test_Top_PBooleanError(self):
        """
        Asserts that when a boolean is passed to top_p an error is thrown.
        """
        for top_p in [True, False]:
            with self.subTest(top_p=top_p):
                with self.assertRaises(RuntimeError) as error:
                    self.request.top_p = top_p
                
                self.assertIsInstance(error.exception, RuntimeError)
    
    def test_Top_PLessThanZero(self):
        """
        Asserts that when an float less than or equal to zero is passed an error is thrown.
        """
        for top_p in range(-10, 0):
            top_p *= 0.1
            with self.subTest(top_p=top_p):
                with self.assertRaises(RuntimeError) as error:
                    self.request.top_p = top_p
                    
                self.assertIsInstance(error.exception, RuntimeError)
    
    def test_Top_PGreaterThanMaximum(self):
        """
        Asserts that when a float greater than the maximum top_p is passed an error is thrown.
        """
        for top_p in range(30, 50):
            top_p *= 0.1
            with self.subTest(top_p=top_p):
                with self.assertRaises(RuntimeError) as error:
                    self.request.top_p = top_p
                    
                self.assertIsInstance(error.exception, RuntimeError)
    
    def test_N(self):
        """
        Asserts that when a valid integer is passed that the correct value is modified
        """
        for n in range(1, 10):
            with self.subTest(n=n):
                self.request.n = n
                
                self.assertEqual(self.request.n, n)
    
    def test_NFloatError(self):
        """
        Asserts that when a float is passed to n an error is thrown.
        """
        for n in range(1, 100):
            n = 0.5 * float(n)
            with self.subTest(n=n):
                with self.assertRaises(RuntimeError) as error:
                    self.request.n = n
                
                self.assertIsInstance(error.exception, RuntimeError)
    
    def test_NBooleanError(self):
        """
        Asserts that when a boolean is passed to n an error is thrown.
        """
        for n in [True, False]:
            with self.subTest(n=n):
                with self.assertRaises(RuntimeError) as error:
                    self.request.n = n
                
                self.assertIsInstance(error.exception, RuntimeError)
    
    def test_NLessThanZero(self):
        """
        Asserts that when an integer less than or equal to zero is passed an error is thrown.
        """
        for n in range(-10, 0):
            with self.subTest(n=n):
                with self.assertRaises(RuntimeError) as error:
                    self.request.n = n
                    
                self.assertIsInstance(error.exception, RuntimeError)
    
    def test_Stream(self):
        """
        Asserts that valid input results in correct data field change.
        """
        for stream in [True, False]:
            with self.subTest(stream=stream):
                self.request.stream = stream
                
                self.assertEqual(self.request.stream, stream)
    
    def test_StreamIntegerFail(self):
        """
        Asserts that an integer input will fail.
        """
        for stream in range(-10, 10):
            with self.subTest(stream=stream):
                with self.assertRaises(RuntimeError) as error:
                    self.request.stream = stream
                
                self.assertIsInstance(error.exception, RuntimeError)
    
    def test_StreamFloatFail(self):
        """
        Asserts that a float input will fail.
        """
        for stream in range(-30, 30):
            stream *= 0.1
            with self.subTest(stream=stream):
                with self.assertRaises(RuntimeError) as error:
                    self.request.stream = stream
                
                self.assertIsInstance(error.exception, RuntimeError)
    
    def test_Echo(self):
        """
        Asserts that valid input results in correct data field change.
        """
        for echo in [True, False]:
            with self.subTest(echo=echo):
                self.request.echo = echo
                
                self.assertEqual(self.request.echo, echo)
    
    def test_EchoIntegerFail(self):
        """
        Asserts that an integer input will fail.
        """
        for echo in range(-10, 10):
            with self.subTest(echo=echo):
                with self.assertRaises(RuntimeError) as error:
                    self.request.echo = echo
                
                self.assertIsInstance(error.exception, RuntimeError)
    
    def test_EchoFloatFail(self):
        """
        Asserts that a float input will fail.
        """
        for echo in range(-30, 30):
            echo *= 0.1
            with self.subTest(echo=echo):
                with self.assertRaises(RuntimeError) as error:
                    self.request.echo = echo
                
                self.assertIsInstance(error.exception, RuntimeError)
    
    def test_Presence_Penalty(self):
        """
        Asserts that when a valid input is made it changes the correct value.
        """
        for pp in range(-20, 21):
            pp *= 0.1
            with self.subTest(pp=pp):
                self.request.presence_penalty = pp
                self.assertEqual(self.request.presence_penalty, pp)
    
    def test_Presence_PenaltyIntegerError(self):
        """
        Asserts that when an integer is passed to presence_penalty an error is thrown.
        """
        for pp in range(-10, 10):
            with self.subTest(pp=pp):
                with self.assertRaises(RuntimeError) as error:
                    self.request.presence_penalty = pp
                
                self.assertIsInstance(error.exception, RuntimeError)
    
    def test_Presence_PenaltyBooleanError(self):
        """
        Asserts that when a boolean is passed to presence_penalty an error is thrown.
        """
        for pp in [True, False]:
            with self.subTest(pp=pp):
                with self.assertRaises(RuntimeError) as error:
                    self.request.presence_penalty = pp
                
                self.assertIsInstance(error.exception, RuntimeError)
    
    def test_Presence_PenaltyLessThanMinimum(self):
        """
        Asserts that when an float less than or equal to zero is passed an error is thrown.
        """
        for pp in range(-30, -22):
            pp *= 0.1
            with self.subTest(pp=pp):
                with self.assertRaises(RuntimeError) as error:
                    self.request.presence_penalty = pp
                    
                self.assertIsInstance(error.exception, RuntimeError)
    
    def test_Presence_PenaltyGreaterThanMaximum(self):
        """
        Asserts that when a float greater than the maximum presence_penalty is passed an error is thrown.
        """
        for pp in range(30, 50):
            pp *= 0.1
            with self.subTest(pp=pp):
                with self.assertRaises(RuntimeError) as error:
                    self.request.presence_penalty = pp
                    
                self.assertIsInstance(error.exception, RuntimeError)

    def test_Frequency_Penalty(self):
        """
        Asserts that when a valid input is made it changes the correct value.
        """
        for fp in range(-20, 21):
            fp *= 0.1
            with self.subTest(fp=fp):
                self.request.frequency_penalty = fp
                self.assertEqual(self.request.frequency_penalty, fp)
    
    def test_Frequency_PenaltyIntegerError(self):
        """
        Asserts that when an integer is passed to presence_penalty an error is thrown.
        """
        for fp in range(-10, 10):
            with self.subTest(fp=fp):
                with self.assertRaises(RuntimeError) as error:
                    self.request.frequency_penalty = fp
                
                self.assertIsInstance(error.exception, RuntimeError)
    
    def test_Frequency_PenaltyBooleanError(self):
        """
        Asserts that when a boolean is passed to frequency_penalty an error is thrown.
        """
        for fp in [True, False]:
            with self.subTest(fp=fp):
                with self.assertRaises(RuntimeError) as error:
                    self.request.frequency_penalty = fp
                
                self.assertIsInstance(error.exception, RuntimeError)
    
    def test_Frequency_PenaltyLessThanMinimum(self):
        """
        Asserts that when an float less than or equal to zero is passed an error is thrown.
        """
        for fp in range(-30, -22):
            fp *= 0.1
            with self.subTest(fp=fp):
                with self.assertRaises(RuntimeError) as error:
                    self.request.frequency_penalty = fp
                    
                self.assertIsInstance(error.exception, RuntimeError)
    
    def test_Frequency_PenaltyGreaterThanMaximum(self):
        """
        Asserts that when a float greater than the maximum frequency_penalty is passed an error is thrown.
        """
        for fp in range(30, 50):
            fp *= 0.1
            with self.subTest(fp=fp):
                with self.assertRaises(RuntimeError) as error:
                    self.request.frequency_penalty = fp
                    
                self.assertIsInstance(error.exception, RuntimeError)

    def test_Best_Of(self):
        """
        Asserts that when a valid integer is passed that the correct value is modified
        """
        for best_of in range(1, 10):
            with self.subTest(best_of=best_of):
                self.request.best_of = best_of
                
                self.assertEqual(self.request.best_of, best_of)
    
    def test_Best_OfFloatError(self):
        """
        Asserts that when a float is passed to best_of an error is thrown.
        """
        for best_of in range(1, 100):
            best_of = 0.5 * float(best_of)
            with self.subTest(best_of=best_of):
                with self.assertRaises(RuntimeError) as error:
                    self.request.best_of = best_of
                
                self.assertIsInstance(error.exception, RuntimeError)
    
    def test_Best_OfBooleanError(self):
        """
        Asserts that when a boolean is passed to n an error is thrown.
        """
        for best_of in [True, False]:
            with self.subTest(best_of=best_of):
                with self.assertRaises(RuntimeError) as error:
                    self.request.best_of = best_of
                
                self.assertIsInstance(error.exception, RuntimeError)
    
    def test_Best_OfLessThanZero(self):
        """
        Asserts that when an integer less than or equal to zero is passed an error is thrown.
        """
        for best_of in range(-10, 0):
            with self.subTest(best_of=best_of):
                with self.assertRaises(RuntimeError) as error:
                    self.request.best_of = best_of
                    
                self.assertIsInstance(error.exception, RuntimeError)
    
    def test_User(self):
        """
        Asserts that valid input results in correct data field change.  
        """
        user = "test-user"
        self.request.user = user
        
        self.assertEqual(self.request.user, user)

    def test_UserIntegerFail(self):
        """
        Asserts that an integer input will fail.
        """
        for user in range(-10, 10):
            with self.subTest(user=user):
                with self.assertRaises(RuntimeError) as error:
                    self.request.user = user
                
                self.assertIsInstance(error.exception, RuntimeError)
    
    def test_UserFloatFail(self):
        """
        Asserts that a float input will fail.
        """
        for user in range(-30, 30):
            user *= 0.1
            with self.subTest(user=user):
                with self.assertRaises(RuntimeError) as error:
                    self.request.user = user
                
                self.assertIsInstance(error.exception, RuntimeError)
    
    def test_UserBooleanFail(self):
        """
        Asserts that when a boolean is passed to n an error is thrown.
        """
        for user in [True, False]:
            with self.subTest(user=user):
                with self.assertRaises(RuntimeError) as error:
                    self.request.user = user
                
                self.assertIsInstance(error.exception, RuntimeError)
    

if __name__ == "__main__":
    unittest.mainloop()
