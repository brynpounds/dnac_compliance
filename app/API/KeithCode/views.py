try:
    from flask import Flask
    from flask_restful import Resource, Api
    from apispec import APISpec
    from marshmallow import Schema, fields
    from apispec.ext.marshmallow import MarshmallowPlugin
    from flask_apispec.extension import FlaskApiSpec
    from flask_apispec.views import MethodResource
    from flask_apispec import marshal_with, doc, use_kwargs
    import requests
    import json
    
    print("All imports are ok............")
except Exception as e:
    print("Error: {} ".format(e))

class KeithControllerSchema(Schema):
    name = fields.String(required=True, description="name is required ", example="Keith")

class KeithController(MethodResource, Resource):
    @doc(description='Echo Experiment for Keith Baldwin', tags=['Placeholder for Keith Code'])
    @use_kwargs(KeithControllerSchema, location=('json'))
    def post(self, **kwargs):
        _message = kwargs.get("name", "default")
        response = {"message":"Good Day " + _message}
        return response

class WeatherControllerSchema(Schema):
    zip = fields.String(required=True, description="zip code",example='66085')
    city = fields.String(required=False, description="city name",example='Overland Park')

class WeatherController(MethodResource, Resource):
    import json
    import requests
    @doc(description='Verification things are working with weather test', tags=['Health and testing Endpoints'])
    @use_kwargs(WeatherControllerSchema, location=('json'))
    def post(self, **kwargs):
        #url = """http://192.241.187.136/data/2.5/weather?zip=10001,us&appid=11a1aac6bc7d01ea13f0d2a8e78c227e"""
        url = """http://192.241.187.136/data/2.5/weather?zip=""" + str(kwargs.get("zip", "10001")) + """,us&appid=11a1aac6bc7d01ea13f0d2a8e78c227e"""
        my_response = requests.get(url)
        our_response_content = my_response.content.decode('utf8')
        proper_json_response = json.loads(our_response_content)
        
        _message = kwargs.get("zip", "10001")
        _message2 = kwargs.get("city", "Overland Park")
        response = {"message":"Weather JSON response for zip code:" + str(_message) + "\n\n" + str(proper_json_response) + "\n\n" + url + _message2}
        return response
 