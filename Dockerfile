FROM debian:latest

# Mettre à jour les paquets et installer Icecast + Liquidsoap
RUN apt update && apt install -y \
    icecast2 \
    liquidsoap \
    curl \
    && apt clean

# Copier les fichiers de configuration
COPY icecast.xml /etc/icecast.xml
COPY liquidsoap_script.liq /usr/local/bin/liquidsoap_script.liq
COPY start.sh /usr/local/bin/start.sh
RUN chmod +x /usr/local/bin/start.sh

# Exposer le port 8000 pour Icecast
EXPOSE 8000

# Démarrer Icecast + Liquidsoap via start.sh
CMD ["/usr/local/bin/start.sh"]
