FROM python:3.8-alpine AS build

ENV PATH="/scripts:${PATH}"

COPY ./requirements.txt requirements.txt
RUN apk add --no-cache --virtual .build-deps \
    ca-certificates gcc postgresql-dev linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev
RUN apk add --update --no-cache --virtual .tmp libc-dev linux-headers
RUN pip install -r requirements.txt
RUN apk del .tmp

RUN mkdir /app
COPY . /app
WORKDIR /app

COPY ./scripts /scripts
RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser -D user
RUN chown -R user:user .
RUN chmod -R 755 /vol/web

USER user

CMD ["entrypoint.sh"]
