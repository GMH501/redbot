FROM alpine:3.7
COPY . /redbot
RUN apk add --no-cache python3 && \
    apk add --no-cache --virtual .build-deps git py3-pip && \
    pip3 install python-redmine && \
    apk del .build-deps && \
    chown -R 1001:1001 /redbot
USER 1001
CMD while true; ls sleep 300 done
