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
        "-i", "https://stream.zeno.fm/hg9eg9q5quzuv",
        "-stream_loop", "-1",
        "-i", "https://superadofm.github.io/Radio_Player_Rodri/background.gif",
        "-filter_complex", "[1:v]scale=1280:720[bg]",
        "-map", "[bg]",
        "-map", "0:a",
        "-c:v", "libx264",
        "-preset", "medium",  # Normal au lieu de ultrafast
        "-b:v", "2500k",
        "-c:a", "aac",
        "-b:a", "128k",
        "-f", "flv",
        "rtmp://a.rtmp.youtube.com/live2/YOUR-STREAM-KEY"
    ]
    subprocess.Popen(command)

if __name__ == "__main__":
    start_stream()
    app.run(host="0.0.0.0", port=10000)  # Port arbitraire
