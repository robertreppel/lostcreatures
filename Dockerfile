FROM elasticsearch:latest
RUN apt-get update && apt-get install -y python
RUN apt-get install -y python-pip python-dev build-essential && pip install elasticsearch
