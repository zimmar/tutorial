from encodings import utf_8
from os import urandom

def venam_genkey(length):
    return bytearray(urandom(length))

def venam_encrypt(plaintext, key):
    return bytearray(
        [ plaintext[i] ^ key[i] for i in range(len(plaintext)) ]
    )
    
def venam_decrypt(chiffretext, key):
    return bytearray(
        [ chiffretext[i] ^ key[i] for i in range(len(chiffretext)) ]
    )

if __name__ == '__main__':
    text = "Hello, World!"
    print(text)
    key = venam_genkey(len(text))
    print(key)
    print(len(text))
    print(len(key))
    ver = venam_encrypt(bytearray(text,'utf-8'), key)
    print(ver)
    ent = venam_decrypt(ver, key)
    
    print("Key: %s" % key)
    print("Verschlüsselt: %s" % ver)
    print("Entschlüsselt: %s" % ent)