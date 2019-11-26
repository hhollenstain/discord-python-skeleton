FROM python:3.6-alpine

COPY . /app
WORKDIR /app

RUN apk add gcc musl-dev libffi-dev libxml2-dev libxslt-dev git make postgresql-dev
RUN make live

CMD ["bot"]
