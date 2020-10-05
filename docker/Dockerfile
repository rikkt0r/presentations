FROM python:3-alpine

ENV PYTHONUNBUFFERED=1

# any package here
RUN pip install pytz
RUN mkdir /app

WORKDIR /app

COPY . /app

EXPOSE 8000

CMD [ "python", "-m", "http.server"]

