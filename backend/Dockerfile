FROM python:3.11.1
ENV PYTHONUNBUFFERED 1
WORKDIR /devdjango_challenge/backend
ADD . /devdjango_challenge/backend
COPY requirements.txt ./
RUN pip install -r requirements.txt
EXPOSE 8000
VOLUME /devdjango_challenge/backend
