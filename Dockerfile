FROM python:3.8-slim-buster

WORKDIR /docker_2

RUN pip install --upgrade pip
COPY req.txt req.txt

RUN pip install -r req.txt
# Installing dependencies
RUN pip install gunicorn
COPY . .


# EXPOSE 8000
# Run the Celery worker
# CMD 

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]