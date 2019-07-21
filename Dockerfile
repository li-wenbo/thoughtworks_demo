FROM python:3.6.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com -r requirements.txt

ARG user=gunicorn
ARG group=gunicorn
ARG uid=1000
ARG gid=1000

ARG HTTP_PORT=8080
ENV HTTP_PORT ${HTTP_PORT}

ARG ENVIRON=test
ENV ENVIRON ${ENVIRON}

RUN addgroup --gid ${gid} ${group} \
    && adduser --uid ${uid} --gid ${gid} --disabled-password --disabled-login --gecos '' --home /var/lib/${user} ${user}

RUN mkdir -p logs && mkdir -p app/logs && chown -R ${uid}:${gid} /app

USER ${user}

# Make port 8080 available to the world outside this container
EXPOSE ${HTTP_PORT}

# Run app.py when the container launches
CMD ["gunicorn", "-c", "gunicorn_conf.py", "server:app"]


