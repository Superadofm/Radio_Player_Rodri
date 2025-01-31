# Playlist automatique
 radio = fallback([
  playlist("http://la-radio-des-artistes-oublies.great-site.net/playlist.m3u")
])

# Connexion au serveur Icecast de Caster.fm
output.icecast(%mp3, 
    host="sapircast.caster.fm", 
    port=17023, 
    password="XshXh8Q5zA", 
    mount="/Wiomg", 
    radio)
