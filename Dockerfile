# syntax=docker/dockerfile:1.4

FROM python:3
EXPOSE 8000
WORKDIR /app 
COPY requirements.txt /app
RUN pip3 install -r requirements.txt
COPY . /app 
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
