# SimplyURL

## Introduction

A python Restful application designed to shorten the URLs.

## Done
- [x] Python Restful file structure.
- [x] Setup gunicorn server.
- [x] Shortener service that will accept a URL as an argument over a REST API and return a shortened URL as a result.
- [x] The URL and shortened URL should be stored in memory by application.
- [x] Implemented the Redirector resource to convert the shortened URL to the Original URL.
- [x] If the same URL is asked again, it should give the same URL as it gave before instead of generating a new one.
- [x] Handled the rare case of favicon.ico being asked.
- [x] Dockerization of the application.
## TODO
- [ ] Instead of in memory, store these things in a text file. [Can you a light DB as well]
- [ ] Swagger documentation.
- [ ] Unit tests.

## How to run

### Docker

* Build the contianer image
```
docker build -t fsimply-url . 
```

* Run the container with `simply-url` image
```
docker run -d -p 5001:5000 --name=simply-url simply-url
```

### Virtual ENV

* Create a virtual env using [Python Virtual Env](https://docs.python-guide.org/dev/virtualenvs/#lower-level-virtualenv)

* Install the requirement
```
pip3 install -r requirements
```

* Run the below gunicorn command to run the Python RestAPI application
```
gunicorn -b 0.0.0.0:5001 api.wsgi:app --timeout=3600 --workers=2 --reload
```

* As we do not have a UI at the moment, please use Postman to send the POST request