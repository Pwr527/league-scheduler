# For more information, please refer to https://aka.ms/vscode-docker-python
FROM ubuntu:22.04

RUN apt update && apt upgrade -y
RUN apt install -y python3-psycopg2 libpq-dev gcc npm
RUN apt install -y python3-pip
RUN npm install --global yarn


EXPOSE 8080

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY backend/requirements.txt .
RUN python3 -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

RUN cd frontend && npm install && npm run build

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "wsgi:app"]
