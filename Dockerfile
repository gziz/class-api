FROM python:3.9-slim

WORKDIR /ml-api

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./models ./models
COPY ./app ./app

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8080", "app.main:app"]

