#!/bin/bash

# Démarrer Icecast
icecast -c /etc/icecast.xml &

# Attendre quelques secondes pour s'assurer qu'Icecast est bien lancé
sleep 5

# Démarrer AutoDJ
liquidsoap /usr/local/bin/liquidsoap_script.liq
