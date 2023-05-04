FROM python:3.12.0a7-slim-bullseye
WORKDIR /app
RUN apt-get update \
    && apt-get -y install libpq-dev gcc
#The previous RUN command is necessary to install the packages for psycog2 (in the requirements file)
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python3", "practice.py", "--host=0.0.0.0"]