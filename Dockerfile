# For GPU, use:
# FROM nvidia/cudagl:11.3.0-devel-ubuntu20.04

# For CPU, use:
FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
	apt-get install -y \
		python3-pip \
		blender

ENV APP_HOME /app
COPY . $APP_HOME
WORKDIR $APP_HOME

RUN pip install Flask
CMD ["python3", "invoker.py"]