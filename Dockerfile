FROM ubuntu:22.04
COPY . /app
WORKDIR /app
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip install -r requirements.txt
CMD python3 main.py
CMD tail -f /dev/null
