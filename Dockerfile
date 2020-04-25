FROM python:3.7-alpine
RUN echo "http://dl-cdn.alpinelinux.org/alpine/latest-stable/main" > /etc/apk/repositories
RUN echo "http://dl-cdn.alpinelinux.org/alpine/latest-stable/community" >> /etc/apk/repositories

RUN apk --no-cache --update-cache add gcc gfortran python python-dev py-pip build-base wget freetype-dev libpng-dev openblas-dev g++
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h

COPY . /
WORKDIR /
RUN pip install -r requirements.txt
CMD /update-and-push.sh

