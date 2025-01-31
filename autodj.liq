# Playlist automatique
radio = playlist("playlist.m3u", fallible=true)

# Connexion au serveur Icecast de Caster.fm
output.icecast(%mp3, 
    host="sapircast.caster.fm", 
    port=17023, 
    password="XshXh8Q5zA", 
    mount="/Wiomg", 
    radio)
