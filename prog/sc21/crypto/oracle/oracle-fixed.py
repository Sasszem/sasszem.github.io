from Crypto.Random import get_random_bytes
from Crypto.Cipher import PKCS1_OAEP, ChaCha20, ARC4, Salsa20, AES, Blowfish
from Crypto.PublicKey import RSA, ECC
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode
from itertools import cycle

from secrets import _KEYS, _API_KEY, _RSA, _ELGAMAL, _NONCES

PEM_START = "-----BEGIN PUBLIC KEY-----"
PEM_END = "-----END PUBLIC KEY-----"

private_key_path = "cert/server-private.pem"
f = open(private_key_path, "r")
server_rsa_key = RSA.import_key(f.read())
f.close()

client_chacha_key = get_random_bytes(32)
client_chacha_nonce = get_random_bytes(12)
client_chacha_cipher = ChaCha20.new(key=client_chacha_key, nonce=client_chacha_nonce)

client_rsa_key = None
server_chacha_cipher = None

def print_first():
    print("Welcome to the my free crypto service!")
    print("Before you can use my service, we must set up and end-to-end encrypted channel.")
    print("First, we will exchange RSA public keys.")
    print("Second, using these public keys, we will exchange encrypted ChaCha keys and nonces.")
    print("Let's get started with the first step.")
    print("")
    print("My 2048 bit RSA public key is the following:")
    print(server_rsa_key.publickey().export_key().decode('utf-8'))
    print("")
    print("Please provide your RSA public key to reach the necessary security level.")
    print("    - It must be 2048 bit")
    print("    - It must be a public key")
    print("    - It must be in PEM format")
    print("    - It should be around 9 lines")
    print("    - Just check mine :)")
    print("")

def get_rsa_key():
    print("Your public key is:")
    line = ""
    public_key = ""
    line_num = 0
    while line != PEM_END and line_num != 15:
        line = input("")
        public_key += line + "\n"
        line_num += 1
    try:
        client_key = RSA.import_key(public_key)
    except:
        print("Something went wrong while loading you key...")
        print("Bye!")
        exit(1)
    print("")
    return client_key

def print_second():
    print("Your public key has been successfully imported!")
    print("Now, I will generate a 32-byte ChaCha20 key and a 12 byte nonce for you to be RFC7539-compliant")
    print("I will encrypt them with your public key.")
    print("Then, you should do the same for me.")
    print("")
    print("Your encrypted ChaCha20 key and nonce for this session is:")
    cipher_rsa = PKCS1_OAEP.new(client_rsa_key)
    enc_chacha_key = cipher_rsa.encrypt(client_chacha_key)
    enc_chacha_nonce = cipher_rsa.encrypt(client_chacha_nonce)
    key = b64encode(enc_chacha_key).decode('utf-8')
    nonce = b64encode(enc_chacha_nonce).decode('utf-8')
    print(key)
    print(nonce)
    print("")

def get_chacha_key():
    print("My encrypted ChaCha20 key and nonce for this session is:")
    try:
        msg = {}
        msg["key"] = input("")
        msg["nonce"] = input("")
        enc_chacha_key = b64decode(msg["key"])
        server_rsa = PKCS1_OAEP.new(server_rsa_key)
        chacha_key = server_rsa.decrypt(enc_chacha_key)
        enc_chacha_nonce = b64decode(msg["nonce"])
        chacha_nonce = server_rsa.decrypt(enc_chacha_nonce)
        chacha_cipher = ChaCha20.new(key=chacha_key,nonce=chacha_nonce)
    except:
        print("Something went wrong while loading you key...")
        print("Bye!")
        exit(1)
    print("")
    return chacha_cipher

def print_third():
    print("The ChaCha20 key and nonce is successfully loaded, thank you.")
    print("From now on, you should send all you messages in ChaCha20 encrypted and Base64 encoded in a JSON format.")
    print("To test this, I will encrypt 'apple' with my key and send it to you along with a MAC divide by a space:")
    encrypted = server_chacha_cipher.encrypt(b'apple')
    msg = b64encode(encrypted).decode('utf-8')
    print(msg)
    print("")
    print("Know you should encrypt 'apple' with your key and send it to me along with the MAC divided by a space:")
    try:
        b64_enc_msg = input("")
        enc_msg = b64decode(b64_enc_msg)
        msg = client_chacha_cipher.decrypt(enc_msg)
        assert(msg == b'apple')
    except:
        print("Something went wrong...")
        print("Bye!")
        exit(1)
    print("")
    print("Very nice, know the service is accessible through this encrypted channel.")

def encrypt_and_print(msg):
    if type(msg) == str:
        msg = msg.encode('utf-8')
    encrypted = server_chacha_cipher.encrypt(msg)
    msg = b64encode(encrypted).decode('utf-8')
    print(msg)

def read_and_decrypt():
    b64_enc_msg = input("")
    enc_msg = b64decode(b64_enc_msg)
    msg = client_chacha_cipher.decrypt(enc_msg)
    return msg

def menu_first():
    encrypt_and_print("What do you want?")
    encrypt_and_print("    - Encrypt (e)")
    encrypt_and_print("    - Decrypt (d)")
    encrypt_and_print("    - Quit (q)")
    msg = read_and_decrypt().decode('utf-8')
    return msg

def menu_second():
    encrypt_and_print("Which cipher do you want? Specify the number.")
    encrypt_and_print("- Symmetric crypto")
    encrypt_and_print("    - Stream ciphers")
    encrypt_and_print("        - ARC4 (0)")
    encrypt_and_print("        - Salsa20 (1)")
    encrypt_and_print("    - Block ciphers")
    encrypt_and_print("        - AES in CBC-mode (2)")
    encrypt_and_print("        - AES in CTR-mode (3)")
    encrypt_and_print("        - Blowfish in ECB-mode (4)")
    encrypt_and_print("        - Blowfish in EAX-mode (5)")
    encrypt_and_print("- Asymmetric crypto")
    encrypt_and_print("    - PKCS OAEP with RSA 2048 (6)")
    encrypt_and_print("    - El Gamal (7)")
    encrypt_and_print("- Other")
    encrypt_and_print("    - XOR (8)")
    choice = int(read_and_decrypt())
    return choice

def read_plaintext():
    encrypt_and_print("Please provide the message you want to encrypt:")
    ret = read_and_decrypt()
    return ret

def read_ciphertext():
    encrypt_and_print("Please provide the message you want to decrypt:")
    ret = read_and_decrypt()
    return ret

def write_plaintext(msg):
    encrypt_and_print("The decrypted message is:")
    encrypt_and_print(msg)

def write_ciphertext(msg):
    encrypt_and_print("The encrypted message is:")
    encrypt_and_print(msg)

def read_and_check_api_key():
    encrypt_and_print("To get the decrypted results, you must provide a valid API key:")
    api_key = read_and_decrypt()
    if api_key == _API_KEY:
        encrypt_and_print("Your API key is valid.")
        return True
    else:
        encrypt_and_print("Your API key is not valid.")
        return False

def handle_arc4(is_enc):
    if is_enc:
        arc4_cipher = ARC4.new(_KEYS.ARC4)
        plaintext = read_plaintext()
        ciphertext = arc4_cipher.encrypt(plaintext)
        write_ciphertext(ciphertext)
    else:
        arc4_cipher = ARC4.new(_KEYS.ARC4)
        ciphertext = read_ciphertext()
        plaintext = arc4_cipher.decrypt(ciphertext)
        if read_and_check_api_key():
            write_plaintext(plaintext)

def handle_salsa20(is_enc):
    if is_enc:
        salsa20_cipher = Salsa20.new(key=_KEYS.Salsa20, nonce=_NONCES.Salsa20)
        plaintext = read_plaintext()
        ciphertext = salsa20_cipher.encrypt(plaintext)
        write_ciphertext(salsa20_cipher.nonce + ciphertext)
    else:
        msg = read_ciphertext()
        nonce = msg[:8]
        ciphertext = msg[8:]
        salsa20_cipher = Salsa20.new(_KEYS.Salsa20, nonce=nonce)
        plaintext = salsa20_cipher.decrypt(ciphertext)
        if read_and_check_api_key():
            write_plaintext(plaintext)

def handle_aes_cbc(is_enc):
    if is_enc:
        aes_cbc_cipher = AES.new(_KEYS.AES_CBC, AES.MODE_CBC)
        plaintext = read_plaintext()
        ciphertext = aes_cbc_cipher.encrypt(pad(plaintext, AES.block_size))
        write_ciphertext(aes_cbc_cipher.iv + ciphertext)
    else:
        msg = read_ciphertext()
        iv = msg[:AES.block_size]
        ciphertext = msg[AES.block_size:]
        aes_cbc_cipher = AES.new(_KEYS.AES_CBC, AES.MODE_CBC, iv=iv)
        plaintext = unpad(aes_cbc_cipher.decrypt(ciphertext), AES.block_size)
        if read_and_check_api_key():
            write_plaintext(plaintext)

def handle_aes_ctr(is_enc):
    if is_enc:
        aes_ctr_cipher = AES.new(_KEYS.AES_CTR, AES.MODE_CTR)
        plaintext = read_plaintext()
        ciphertext = aes_ctr_cipher.encrypt(plaintext)
        write_ciphertext(aes_ctr_cipher.nonce + ciphertext)
    else:
        msg = read_ciphertext()
        nonce = msg[:AES.block_size//2]
        ciphertext = msg[AES.block_size//2:]
        aes_ctr_cipher = AES.new(_KEYS.AES_CTR, AES.MODE_CTR, nonce=nonce)
        plaintext = aes_ctr_cipher.decrypt(ciphertext)
        if read_and_check_api_key():
            write_plaintext(plaintext)

def handle_blowfish_ecb(is_enc):
    if is_enc:
        blowfish_ecb_cipher = Blowfish.new(_KEYS.Blowfish_ECB, Blowfish.MODE_ECB)
        plaintext = read_plaintext()
        ciphertext = blowfish_ecb_cipher.encrypt(pad(plaintext, Blowfish.block_size))
        write_ciphertext(ciphertext)
    else:
        ciphertext = read_ciphertext()
        blowfish_ctr_cipher = Blowfish.new(_KEYS.Blowfish_ECB, Blowfish.MODE_ECB)
        plaintext = unpad(blowfish_ctr_cipher.decrypt(ciphertext), Blowfish.block_size)
        if read_and_check_api_key():
            write_plaintext(plaintext)

def handle_blowfish_eax(is_enc):
    if is_enc:
        blowfish_eax_cipher = Blowfish.new(_KEYS.Blowfish_EAX, Blowfish.MODE_EAX)
        plaintext = read_plaintext()
        ciphertext = blowfish_eax_cipher.encrypt(plaintext)
        write_ciphertext(blowfish_eax_cipher.nonce + ciphertext)
    else:
        msg = read_ciphertext()
        nonce = msg[:Blowfish.block_size*2]
        ciphertext = msg[Blowfish.block_size*2:]
        blowfish_eax_cipher = Blowfish.new(_KEYS.Blowfish_EAX, Blowfish.MODE_EAX, nonce=nonce)
        plaintext = blowfish_eax_cipher.decrypt(ciphertext)
        if read_and_check_api_key():
            write_plaintext(plaintext)

def handle_rsa(is_enc):
    if is_enc:
        rsa_key = RSA.construct((_RSA.n, _RSA.e, _RSA.d, _RSA.p, _RSA.q))
        rsa_cipher = PKCS1_OAEP.new(rsa_key)
        plaintext = read_plaintext()
        ciphertext = rsa_cipher.encrypt(plaintext)
        write_ciphertext(ciphertext)
    else:
        ciphertext = read_ciphertext()
        rsa_key = RSA.construct((_RSA.n, _RSA.e, _RSA.d, _RSA.p, _RSA.q))
        rsa_cipher = PKCS1_OAEP.new(rsa_key)
        plaintext = rsa_cipher.decrypt(ciphertext)
        if read_and_check_api_key():
            write_plaintext(plaintext)

def el_gamal_encrypt(msg, g, q, y, h):
    s = pow(h, y, q)
    c1 = pow(g, y, q)
    c2 = (s * int.from_bytes(msg,'big') % q)
    c1 = int.to_bytes(c1, 64, 'big').lstrip(b'\x00')
    c2 = int.to_bytes(c2, 64, 'big').lstrip(b'\x00')
    return c1, c2

def el_gamal_decrypt(en_msg, q, x, c1):
    s = pow(c1, x, q)
    msg = int.to_bytes((en_msg * pow(s, -1, q)) % q, 64, 'big')
    msg = msg.lstrip(b'\x00')
    return msg

def handle_el_gamal(is_enc):
    if is_enc:
        plaintext = read_plaintext()
        c1, c2 = el_gamal_encrypt(plaintext, _ELGAMAL.g, _ELGAMAL.q, _ELGAMAL.y, _ELGAMAL.h)
        encrypt_and_print("The encrypted message is (c1, c2):")
        encrypt_and_print(c1)
        encrypt_and_print(c2)
    else:
        encrypt_and_print("Please provide the message you want to decrypt (c1, c2):")
        c1 = read_and_decrypt()
        c2 = read_and_decrypt()
        plaintext = el_gamal_decrypt(int.from_bytes(c2, 'big'), _ELGAMAL.q, _ELGAMAL.x, int.from_bytes(c1, 'big'))
        if read_and_check_api_key():
            write_plaintext(plaintext)

def xor(data, key):
    return bytes(''.join([chr(a^b) for a, b in zip(data, cycle(key))]), encoding='utf-8')

def handle_xor(is_enc):
    if is_enc:
        plaintext = read_plaintext()
        ciphertext = xor(plaintext, _KEYS.XOR)
        write_ciphertext(ciphertext)
    else:
        ciphertext = read_ciphertext()
        plaintext = xor(ciphertext, _KEYS.XOR)
        if read_and_check_api_key():
            write_plaintext(plaintext)

cipher_menu_handlers = [
    handle_arc4,
    handle_salsa20,
    handle_aes_cbc,
    handle_aes_ctr,
    handle_blowfish_ecb,
    handle_blowfish_eax,
    handle_rsa,
    handle_el_gamal,
    handle_xor
]

if __name__=="__main__":
    print_first()
    client_rsa_key = get_rsa_key()
    print_second()
    server_chacha_cipher = get_chacha_key()
    print_third()
    while True:
        try:
            choice = menu_first()
            if choice == "e":
                choice = menu_second()
                cipher_menu_handlers[choice](is_enc=True)
            elif choice == "d":
                choice = menu_second()
                cipher_menu_handlers[choice](is_enc=False)
            elif choice == "q":
                encrypt_and_print("Thanks for using my service!")
                encrypt_and_print("Bye")
                break
            else:
                encrypt_and_print("Unknown command")
        except:
            encrypt_and_print("Something went wrong...")
