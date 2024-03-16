import qrcode as q
i=q.make("https://www.linkedin.com/in/udhayabaskarrk?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app")
i.save("qr.png")
print("QR code generated")