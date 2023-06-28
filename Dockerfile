FROM python:3.9-slim-buster
WORKDIR /app
COPY . /app
RUN pip3 install -r requirement.txt
CMD python3 hello.py
