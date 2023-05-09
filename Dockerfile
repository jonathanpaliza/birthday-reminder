FROM python:3.11.3

WORKDIR /app

COPY . ./

RUN pip install -r requirements.txt

CMD ["python", "app.py"]