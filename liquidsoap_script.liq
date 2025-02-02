# Configuration du serveur Icecast
server_host = "localhost"
server_port = 8000
server_password = "hackme"
server_mount = "/stream"

# Charger la playlist en boucle depuis GitHub
playlist_url = "https://superadofm.github.io/Radio_Player_Rodri/playlist.m3u"
auto_dj = playlist(playlist_url, random=true, reload=60.)

# Détecter si un live est en cours (depuis un logiciel comme BUTT ou Mixxx)
live = input.harbor("8001", password="hackme")

# Si un live est détecté, il remplace l'Auto DJ automatiquement
radio = fallback(track_sensitive=false, [
