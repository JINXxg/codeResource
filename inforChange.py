from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa

private_keyA=rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,#holy shit I forget these this is a function
    backend=default_backend()
)
public_keyA=private_keyA.public_key()

private_keyB=rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
public_keyB=private_keyB.public_key()

private_keyC=rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
public_keyC=private_keyC.public_key()

message=b"Hello Ailice, I am so soryy for hurt you\n"
ciphertext=public_keyB.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

modifymessage=b"you are so stupid ailice\n"
modifyciphertext=public_keyB.encrypt(
    modifymessage,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
modifyplaintext=private_keyB.decrypt(
    modifyciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print("this is origin message\n",message)
print("this is modify message\n",modifymessage)
print("this is mesagge Alice see\n",)