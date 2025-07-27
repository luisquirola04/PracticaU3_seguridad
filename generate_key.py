from Crypto.PublicKey import RSA

# par de claves (2048 bits)
key = RSA.generate(2048)

private_key = key.export_key(
    passphrase="PracticaU3",
    pkcs=8,
    protection="scryptAndAES128-CBC"
)
with open("privada.pem", "wb") as f:
    f.write(private_key)

# Guardar clave pública
public_key = key.publickey().export_key()
with open("publica.pem", "wb") as f:
    f.write(public_key)

print("Claves generadas")
