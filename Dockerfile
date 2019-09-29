FROM python:3.7.4-buster

RUN adduser --disabled-password mappad

WORKDIR /home/mappad

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn
RUN pip install psycopg2

COPY app app
COPY migrations migrations
COPY application.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP application.py

RUN chown -R mappad:mappad ./
USER mappad

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
