import json
import requests
from dotenv import load_dotenv
load_dotenv()

try:
    from API import (app,
                     api,
                     HeathController,docs,
                     KeithController,
                     WeatherController
                     )
except Exception as e:
    print("Modules are Missing : {} ".format(e))

api.add_resource(HeathController, '/health_check')
docs.register(HeathController)

api.add_resource(KeithController, '/keith_code')
docs.register(KeithController)

api.add_resource(WeatherController, '/check_weather')
docs.register(WeatherController)
