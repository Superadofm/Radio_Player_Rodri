#!/bin/bash

# Télécharger la playlist depuis GitHub
wget -O playlist.txt "https://raw.githubusercontent.com/Superadofm/Radio_Player_Rodri/main/playlist.txt"

# Lancer le stream avec la playlist
while true; do
    ffmpeg -re -stream_loop -1 -f concat -safe 0 -i playlist.txt \
           -ignore_loop 0 -i "https://raw.githubusercontent.com/Superadofm/Radio_Player_Rodri/main/background.gif" \
           -filter_complex "[1:v]scale=1280:720:flags=lanczos,format=yuva420p[v];[v]loop=-1:1:0[vout]" \
           -map "[vout]" -map 0:a -c:v libx264 -crf 23 -preset veryfast -c:a aac -b:a 128k \
           -f flv "rtmp://a.rtmp.youtube.com/live2/VOTRE_CLE_STREAM"
    sleep 5  # Relance en cas d'erreur
done
