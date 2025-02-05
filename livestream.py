from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return "Le live est actif !"

def start_stream():
    command = [
        "ffmpeg",
        "-re",
        "-i", "https://stream.zeno.fm/hg9eg9q5quzuv",  # Flux Zeno.fm
        "-stream_loop", "-1",
        "-i", "https://superadofm.github.io/Radio_Player_Rodri/background.gif",  # GIF de fond
        "-filter_complex", "[1:v]scale=1920:1080[bg]",  # Passage en Full HD (1080p)
        "-map", "[bg]",
        "-map", "0:a",
        "-c:v", "libx264",
        "-preset", "slow",  # Qualité améliorée (moins de pertes)
        "-b:v", "6000k",  # Débit vidéo augmenté (6 Mbps)
        "-maxrate", "6500k",  # Débit maximal pour éviter les fluctuations
        "-bufsize", "12000k",  # Tampon plus grand pour éviter les coupures
        "-c:a", "aac",
        "-b:a", "320k",  # Débit audio très élevé (qualité maximale)
        "-f", "flv",
        "rtmp://a.rtmp.youtube.com/live2/q0m7-ev92-uh81-juw8-ctb8"  # Remplace avec ta clé YouTube
    ]
    subprocess.Popen(command)

if __name__ == "__main__":
    start_stream()
    app.run(host="0.0.0.0", port=10000)  # Port arbitraire
