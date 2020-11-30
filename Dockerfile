FROM python:3.6

ENV PYTHONUNBUFFERED 1
RUN mkdir -p /usr/src/backend
WORKDIR /usr/src/backend
ADD . /usr/src/backend/

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["python3","manage.py","migrate"]
CMD ["python3","manage.py","runserver"]

# EXPOSE 8000