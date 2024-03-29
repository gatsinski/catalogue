FROM python:3.9.9-buster
RUN apt update && apt install -y gettext
RUN pip3 install pipenv gunicorn

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv install --system

COPY . .

ENV DJANGO_ENV=production

EXPOSE 8002

CMD sh docker-entrypoint.sh
