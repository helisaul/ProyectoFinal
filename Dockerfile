FROM python:3.12.1-alpine3.18

ENV PYTHONBUFFERED=1
WORKDIR /django
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . . 
CMD python manage.py runserver 0.0.0.0:8000