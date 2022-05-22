try:
    from api.extensions import hashidsObj, ma
    from flask_restful import Resource
    import os
    from flask import request, redirect
    import validators
    from api.resources.helper import URLMapping
    from api.config import URL_MAP_FILE
except Exception as e:
    print("Error: {} ".format(e))


class LinkShortnerRequestSchema(ma.Schema):
    url = ma.Url(required=True, description="LinkShortner")


class LinkShortnerResponseSchema(ma.Schema):
    url = ma.Url()
    short_url = ma.Url()


class LinkShortner(Resource):
    """Link shortner
    ---
    post:
      tags:
        - api
      summary: Generates a Shortened URL
      description: Generates a Shortened URL for the provided URL
      requestBody:
        content:
          application/json:
            schema:
              LinkShortnerRequestSchema
      responses:
        201:
          content:
            application/json:
              schema: LinkShortnerResponseSchema      
        400:
            description: Not a valid URL provided.
    """

    '''
    A post method which:
    1. Accepts a URL
    2. Validates the URL
    3. Get the Dictonary from a file
    4. Generate a short URL
    5. Store the mapping of Orignal URL and short URL in a JSON file.
    '''

    def post(self):
        jsonData = request.get_json()
        # Checking if the jsonData is empty
        if not jsonData and not jsonData["url"]:
            return {'message': 'Not a valid URL provided.'}, 400

        url = jsonData["url"]

        # Checking if the provided URL is correct
        if not validators.url(url):
            return {'message': 'Not a valid URL provided.'}, 400

        # Get the URL mapping from url_map.json file
        um = URLMapping()
        urlMapping = um.get_url_mapping(URL_MAP_FILE)
        # Checking if the provided URL already exist in the Dictonary
        if url in urlMapping:
            hashId = urlMapping[url]
        else:
            urlMapping[url] = None
            urlId = len(urlMapping)
            hashId = hashidsObj.encode(urlId)
            urlMapping[url] = hashId

        shortUrl = request.host_url + "s/" + hashId
        um.set_url_mapping(URL_MAP_FILE, urlMapping)
        responseSchema = LinkShortnerResponseSchema()
        return responseSchema.dump({"url": url, "short_url": shortUrl}), 201


class Redirector(Resource):
    """Single object resource
    ---
    get:
      tags:
        - api
      summary: Convert the Short URL to Original URL
      description: Takes the short URL map and redirect to the Original URL
      parameters:
        - in: path
          name: shortenedId
          schema:
            type: string
      responses:
        302:
          description: "Redirection response"
          headers:
            Location:
                description: "URL to redirect"
                type: url
        200:
            description: "Response from redirected URL"
        400:
          description: Provided URL does not exist. Please verify the URL.
    """
    '''
    Redirector is a resource with GET method which:
    1. Loads the URL mapping from a text file
    2. Search the Dictonary for shortened URL ID.
    3. Redirect to the Original URL
    '''

    def get(self, shortenedId):
        um = URLMapping()
        urlMapping = um.get_url_mapping(URL_MAP_FILE)
        # Searching across the Dictonary for the value matching the shortenedURL so that we may send the key.
        for key, value in urlMapping.items():
            if value == shortenedId:
                return redirect(key)
        return {'message': 'Provided URL does not exist. Please verify the URL.'}, 400