FROM python:3

ADD bot.py /

ADD config.py /

RUN pip install metar pytelegrambotapi requests

CMD [ "python", "/bot.py" ]
