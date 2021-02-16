FROM python:latest

COPY ./whirlpkgs /src

WORKDIR /src

RUN pip install -r requirements.txt

EXPOSE 8000


