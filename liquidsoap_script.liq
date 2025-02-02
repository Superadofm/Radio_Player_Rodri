# Définition des sources de musique (playlist)
playlist = playlist("/path/to/playlist.m3u")

# Connexion à Icecast en utilisant un mot de passe pour l'auto-diffusion
auto_dj_output = output.icecast(
    %mp3, 
    host="127.0.0.1", 
    port=8000, 
    password="hackme", 
    mount="stream.mp3", 
    playlist
)

# Créer un flag qui va surveiller si un flux en direct (live) est actif
# Si quelqu'un se connecte en direct, le flux AutoDJ s'arrête et commence à diffuser en direct
live_input = input.icecast(
    host="127.0.0.1", 
    port=8000, 
    mount="live", 
    password="hackme"
)

# Condition pour vérifier si le flux en direct est actif
# Si une connexion en direct est détectée, on arrête l'AutoDJ et on passe en live
output_live = 
    if (live_input != null) then
        live_input  # Si le flux en direct est actif, on diffuse le live
    else
        auto_dj_output  # Si pas de flux en direct, on reprend l'AutoDJ
    end

# Diffusion
output_live
