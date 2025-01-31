settings.log.file = "autodj.log"
set("log.level", 3)

# Playlist automatique
radio = playlist("https://raw.githubusercontent.com/Superadofm/Radio_Player_Rodri/refs/heads/main/playlist.m3u")

# Connexion au serveur Icecast de Caster.fm
output.icecast(%mp3, 
    host="sapircast.caster.fm", 
    port=17023, 
    password="XshXh8Q5zA", 
    mount="/Wiomg", 
    radio)
