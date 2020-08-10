FROM python:3.7

RUN apt-get update && apt-get -y install \
    libpq-dev

WORKDIR /app
ADD    ./requirements.txt   /app/
RUN    pip3 install --default-timeout=100 -r requirements.txt

ADD    ./djangosample   /app/djangosample/
ADD    ./manage.py      /app/

ENV     PYTHONUNBUFFERED 0

CMD ["python", "manage.py", "runserver", "0:8888"]
