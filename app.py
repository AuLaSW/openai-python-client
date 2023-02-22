from os import environ
# import openai
from tests.unit.fixture import api
from openaiclient.controller.controller import Controller

# get API key from usr folder
# openai.api_key = environ["OPENAI_API_KEY"]

controller = Controller(api)

controller.start()