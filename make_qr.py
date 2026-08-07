import sys, qrcode
url = sys.argv[1] if len(sys.argv) > 1 else input("Paste your live GitHub Pages URL: ").strip()
img = qrcode.make(url)
img.save("assets/qr-profile.png")
print("Created assets/qr-profile.png for", url)
