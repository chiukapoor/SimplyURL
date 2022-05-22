# SimplyURL

[![Simply URL build and Test](https://github.com/C-Society/SimplyURL/workflows/simply-url/badge.svg)](https://github.com/C-Society/SimplyURL/actions)

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
- [x] Instead of in memory, store these things in a text file.
- [x] Added error handling in file handling and import statement.
- [x] Swagger documentation.
- [x] Unit tests.

## TODO

- [ ] As it is hard to scale the application while using a file to store the data, rather we may use a DB such as Postgres or SQL lite.

## How to run and test the application

- Run the Flask application with one of the below methods

- Docker

  - Build the contianer image

  ```
  docker build -t simply-url .
  ```

  - Run the container with `simply-url` image

  ```
  docker run -d -p 5002:5000 --name=simply-url  -v $PWD/url_mapping.json:/code/url_mapping.json simply-url
  ```

- Python virtual environment

  - Create a virtual env using [Python Virtual Env](https://docs.python-guide.org/dev/virtualenvs/#lower-level-virtualenv)

  - Install the requirement

  ```
  pip3 install -r requirements
  ```

  - Run the below gunicorn command to run the Python RestAPI application

  ```
  gunicorn -b 0.0.0.0:5001 api.wsgi:app --timeout=3600 --workers=2 --reload
  ```

  - As we do not have a UI at the moment, please use Postman to send the POST request

- Once the Flask application is up and running use the below URL to access the Swagger UI

```
http://0.0.0.0:5001/swagger-ui
```

- To run the unit tests use the command below

```
pytest
```
