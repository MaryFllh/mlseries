FROM python:3.9-slim as py39slim
RUN apt-get update -y && apt-get install -y git

WORKDIR /ml
COPY ./ml/requirements.txt /ml
RUN pip install -r requirements.txt --no-cache-dir

COPY ./ml /ml

ENTRYPOINT ["/bin/bash", "-c"]