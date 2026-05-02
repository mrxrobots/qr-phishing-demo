import qrcode
import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

url = f"http://{ip}:8080"
qr = qrcode.make(url)
qr.save("qr.png")
print(f"QR Generated: {url}")
print("Scan qr.png with your phone!")