FROM ubuntu:20.04

RUN apt-get update && apt-get install -y icecast2

# Configure Icecast
COPY icecast.xml /etc/icecast2/icecast.xml

EXPOSE 8000

CMD ["icecast", "-c", "/etc/icecast2/icecast.xml"]
