from os import environ
import openai
from tests.unit.fixture import api
from openaiclient.controller import Controller
from openaiclient.controller.controller import StartKey as sk

controller = Controller(api)

# get API key from environment
try:
    openai.api_key = environ["OPENAI_API_KEY"]
    controller.start()
except Exception as err:
    controller.start(sk.NO_API_KEY)
