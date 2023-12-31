FROM python:3.8.17-bullseye

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

ARG pymongourl
ENV pymongourl=$pymongourl

RUN python main.py

CMD ["python3", "app.py"]
