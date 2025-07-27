from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import re
from binascii import unhexlify

priv_key = RSA.import_key(open("privada.pem").read(), passphrase="PracticaU3")
decipher = PKCS1_OAEP.new(priv_key)

with open("archivo.txt", "r") as f:
    contenido = f.read()

contenido_modificado = re.sub(
    r"Cedula: ([0-9a-fA-F]+)",
    lambda m: f"Cedula: {decipher.decrypt(unhexlify(m.group(1))).decode()}",
    contenido
)
contenido_modificado = re.sub(
    r"Monto_Banco: ([0-9a-fA-F]+)",
    lambda m: f"Monto_Banco: {decipher.decrypt(unhexlify(m.group(1))).decode()}",
    contenido_modificado
)

with open("restaurado_datos.txt", "w") as f:
    f.write(contenido_modificado)
