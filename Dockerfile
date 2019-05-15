FROM sentry:8.15

COPY requirements.txt /tmp
RUN set -x \
    && pip install -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt
