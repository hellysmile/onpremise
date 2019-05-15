FROM sentry:9.1.1

COPY requirements.txt /tmp
RUN set -x \
    && pip install -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt
