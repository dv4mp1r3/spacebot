FROM python:3.11.3-alpine3.18 as python311-alpine

WORKDIR /opt/spacebot

RUN addgroup -S spacebot \
    && adduser \
    --disabled-password \
    --gecos "" \
    --home /home/spacebot \
    --ingroup spacebot \
    --uid "1000" \
    spacebot

COPY --chown=spacebot:spacebot ./.env ./residents.csv ./requirements.txt ./bot.py /openapi.yaml /service-account.json ./
ADD --chown=spacebot:spacebot logic logic
ADD --chown=spacebot:spacebot openapi_client openapi_client

RUN pip3 install -r requirements.txt

USER spacebot

CMD ["python3", "bot.py"]