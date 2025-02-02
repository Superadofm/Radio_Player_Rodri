FROM ubuntu:20.04

RUN apt-get update && apt-get install -y icecast2

# Configure Icecast
COPY icecast.xml /etc/icecast2/icecast.xml

# Copie du fichier de configuration
COPY liquidsoap_script.liq /etc/liquidsoap/liquidsoap_script.liq

EXPOSE 8000

CMD ["icecast2 -b -c /etc/icecast2/icecast.xml"]

CMD ["liquidsoap", "/etc/liquidsoap/liquidsoap_script.liq"]
