# Configuration Icecast
settings.log.file = false
set("init.daemon", false)

# Définir les sources
playlist = playlist("/usr/local/bin/playlist.m3u", reload=1)
live = input.http("http://localhost:8000/live", on_error=fallible=false)

# Vérifier si un live est en cours, sinon AutoDJ
radio = fallback(track_sensitive=false, [live, playlist])

# Envoyer le flux à Icecast
output.icecast(%mp3, host="localhost", port=8000, password="hackme", mount="/stream", radio)
