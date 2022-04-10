FROM debian:buster
MAINTAINER Lukas Plevac

RUN apt-get update && \
    apt-get -y upgrade && DEBIAN_FRONTEND=noninteractive apt-get -y install \
    python3 python3-pip && \
    pip3 install --upgrade setuptools pip && \
    pip3 install Flask && \
    pip3 install r2server && \
    pip3 install requests && \
    pip3 install mysql-connector-python && \
    pip3 install maidenhead

#add system
ADD src/. /r2cloud_public

EXPOSE 5000
VOLUME ["/r2cloud_public/setting.py"]

ADD entry.sh /

CMD ["/bin/bash", "/entry.sh"]