#!/bin/bash

# Lancer Icecast en arrière-plan
/usr/bin/icecast2 -c /etc/icecast.xml &

# Attendre quelques secondes pour s'assurer qu'Icecast est bien lancé
sleep 5

# Lancer Liquidsoap
/usr/bin/liquidsoap /usr/local/bin/liquidsoap_script.liq
