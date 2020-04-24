FROM python:3-slim

RUN pip install flask
COPY . /app
VOLUME /context

CMD ["python", "/app/app.py"]