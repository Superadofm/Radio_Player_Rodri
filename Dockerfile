FROM debian:latest

# Installer Icecast et Liquidsoap
RUN apt update && apt install -y icecast2 liquidsoap

# Copier les fichiers de configuration
COPY icecast.xml /etc/icecast.xml
COPY liquidsoap_script.liq /usr/local/bin/liquidsoap_script.liq
COPY start.sh /usr/local/bin/start.sh
RUN chmod +x /usr/local/bin/start.sh

# Exposer les ports
EXPOSE 8000

# Lancer Icecast + Liquidsoap
CMD ["/usr/local/bin/start.sh"]
