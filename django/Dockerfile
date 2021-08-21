FROM python:3.8.10

RUN pip install django

COPY ./tutorial_project /app
WORKDIR /app

RUN ls -la

EXPOSE 8000

CMD python manage.py runserver 0:8000
