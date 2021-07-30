FROM python:alpine

# ENV API_ID
# ENV API_HASH
# ENV BOT_TOKEN

RUN addgroup bot \
    && adduser -s /bin/sh -D -G bot bot

WORKDIR /usr/src/bot
COPY --chown=bot:bot . .

RUN chown bot:bot /usr/src/bot \
    && apk add --no-cache --virtual .build-deps build-base libffi-dev libretls-dev gcc \
    && pip install -r requirements.txt \
    && apk del .build-deps

USER bot

CMD python ./bot.py ${API_ID} ${API_HASH} ${BOT_TOKEN}
