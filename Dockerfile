# For GPU, use:
FROM nvidia/cuda:12.8.0-base-ubuntu24.04
# For CPU-only, use:
# FROM ubuntu:24.04

LABEL Title="Blender in Docker wiht GPU, as a service"

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
		python3-pip \
		blender

ENV APP_HOME=/app
COPY . $APP_HOME
WORKDIR $APP_HOME

RUN apt-get install -y python3-flask

#RUN pip install Flask
CMD ["python3", "invoker.py"]
