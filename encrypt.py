from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import re

# Cargar clave pública
key = RSA.import_key(open("publica.pem").read())
cipher = PKCS1_OAEP.new(key)

with open("archivo.txt", "r") as f:
    contenido = f.read()

contenido_modificado = re.sub(
    r"Cedula: (.+)",
    lambda m: f"Cedula: {cipher.encrypt(m.group(1).encode()).hex()}",
    contenido
)
contenido_modificado = re.sub(
    r"Monto_Banco: (.+)",
    lambda m: f"Monto_Banco: {cipher.encrypt(m.group(1).encode()).hex()}",
    contenido_modificado
)

with open("archivo.txt", "w") as f:
    f.write(contenido_modificado)
