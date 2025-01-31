radio = playlist("https://raw.githubusercontent.com/Superadofm/Radio_Player_Rodri/refs/heads/main/playlist.m3u")

output.icecast(%mp3, host="radio-player-rodri.fly.dev", port=8000, password="source_password", mount="/stream", radio)
