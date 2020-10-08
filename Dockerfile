FROM alpine:3.7
RUN apk add --no-cache python3 && \
    apk add --no-cache --virtual .build-deps git py3-pip && \
    pip3 install python-redmine && \
    git clone https://github.com/GMH501/redbot.git && \
    apk del .build-deps && \
    chown -R 1001:1001 /redbot
USER 1001
CMD /bin/sh
