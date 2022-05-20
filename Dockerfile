FROM python:3.9-slim-buster
RUN mkdir /code
WORKDIR /code

COPY requirements.txt entrypoint.sh ./
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY api api/

EXPOSE 5000

RUN ["chmod", "+x", "entrypoint.sh"]

ENTRYPOINT [ "./entrypoint.sh" ]