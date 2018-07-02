FROM python

RUN apt-get update && \
	apt-get install -y \
		blender

ENV APP_HOME /app
COPY . $APP_HOME
WORKDIR $APP_HOME

RUN pip install Flask

EXPOSE 8080

CMD ["python", "app.py"]