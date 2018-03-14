FROM python:3
RUN apt-get update
RUN apt-get install -y python3-pip
RUN apt-get clean

COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt
COPY . /app
WORKDIR /app
EXPOSE 5000
CMD ["python3", "run.py"]
