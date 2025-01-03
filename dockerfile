FROM python:3.12.8-bullseye

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY /app/ /app

CMD ["python", "main.py"]
