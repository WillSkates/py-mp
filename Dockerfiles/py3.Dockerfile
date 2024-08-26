#!/bin/bash

FROM scratch

ADD alpine.tar.gz /

RUN echo "https://uk.alpinelinux.org/alpine/v3.20/main" > /etc/apk/repositories
RUN echo "https://uk.alpinelinux.org/alpine/v3.20/community" >> /etc/apk/repositories

RUN apk add python3 py3-pip bash

COPY entrypoint.sh /entrypoint.sh

RUN python --version && pip --version && mkdir /work && chmod +x /entrypoint.sh


ENTRYPOINT ["/entrypoint.sh"]
WORKDIR "/work"
