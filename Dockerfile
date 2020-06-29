FROM python:3.7-alpine
LABEL version="0.1"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
# permanent dependencies
RUN apk add --update --no-cache postgresql-client jpeg-dev
# dependencies just needed for installing Python modules (Pillow needs: musl-dev zlib zlib-dev)
RUN apk add --update --no-cache --virtual .tmp-build-deps \
        gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app

# /vol indicates volume that can be shared with other containers (e.g. nginx web server that has to serve the media files)
# -p: create all subdirectories if they don't exist
RUN mkdir -p /vol/web/media
# static data like e.g. javascipt, CSS
RUN mkdir -p /vol/web/static
RUN adduser -D user
# set ownership to custom user (must be done before changing from 'root' to 'user' via USER directive)
RUN chown -R user:user /vol/
RUN chmod -R 755 /vol/web
USER user
