from api.extensions import hashidsObj
from flask_restful import Resource
from flask import request

linkMaps = {}
class LinkShortner(Resource):
    def post(self):
        jsonData = request.get_json()
        if not jsonData:
            return {'message': 'No URL provided'}, 400
        
        url = jsonData["URL"]

        linkMaps[url] = None

        urlId = len(self.linkMaps)
        hashId = hashidsObj.encode(urlId)
        short_url = request.host_url + hashId
        
        linkMaps[url] = short_url

        return {"url":url, "short_url": short_url}, 200

class Redirector(Resource):
    def get():
        pass