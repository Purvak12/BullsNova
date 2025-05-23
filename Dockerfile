FROM python:3.10-slim

COPY requirements.txt /setup/

WORKDIR /setup

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python"]

CMD ["application.py"]