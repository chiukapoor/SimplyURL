from api.extensions import hashidsObj
from flask_restful import Resource
import os
from flask import request, redirect
import validators

linkMaps = {}
class LinkShortner(Resource):
    def post(self):
        jsonData = request.get_json()

        # Checking if the jsonData is empty
        if not jsonData:
            return {'message': 'No data provided'}, 400
        
        url = jsonData["URL"]

        # Checking if the provided URL is correct
        if not validators.url(url):
            return {'message': 'Not a valid URL provided.'}, 400

        # Checking if the provided URL already exist in the Dictonary
        if url in linkMaps:
            shortUrl = linkMaps[url]
        else:
            linkMaps[url] = None
            urlId = len(linkMaps)
            hashId = hashidsObj.encode(urlId)
            shortUrl = request.host_url + hashId
            linkMaps[url] = shortUrl

        return {"url":url, "short_url": shortUrl}, 200

class Redirector(Resource):
    def get(self, shortenedURL):
        # Rare scenario where favicon is requested. Currently we are returing a 200
        if shortenedURL == "favicon.ico":
            return {"Pass"}, 200

        # Searching across the Dictonary for the value matching the shortenedURL so that we may send the key.
        for key, value in linkMaps.items():
            if value == request.host_url+shortenedURL:
                return redirect(key)
        return {'message': 'Provided URL does not exist. Please verify the URL.'}, 400
