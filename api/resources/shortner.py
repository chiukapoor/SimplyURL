from api.extensions import hashidsObj
from flask_restful import Resource
import os
from flask import request, redirect
import validators
from api.resources.helper import URLMapping
from api.config import URL_MAP_FILE

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
        
        # Get the URL mapping from url_map.json file
        um = URLMapping()
        urlMapping = um.get_url_mapping(URL_MAP_FILE)
        # Checking if the provided URL already exist in the Dictonary
        if url in urlMapping:
            shortUrl = urlMapping[url]
        else:
            urlMapping[url] = None
            urlId = len(urlMapping)
            hashId = hashidsObj.encode(urlId)
            shortUrl = request.host_url + hashId
            urlMapping[url] = shortUrl
        
        um.set_url_mapping(URL_MAP_FILE, urlMapping)
        return {"url":url, "short_url": shortUrl}, 200

class Redirector(Resource):
    def get(self, shortenedURL):
        # Rare scenario where favicon is requested. Currently we are returing a 200
        if shortenedURL == "favicon.ico":
            return {"Pass"}, 200
        
        um = URLMapping()
        urlMapping = um.get_url_mapping(URL_MAP_FILE)
        # Searching across the Dictonary for the value matching the shortenedURL so that we may send the key.
        for key, value in urlMapping.items():
            if value == request.host_url+shortenedURL:
                return redirect(key)
        return {'message': 'Provided URL does not exist. Please verify the URL.'}, 400
