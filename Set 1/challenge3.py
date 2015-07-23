import binascii
from Crypto.Util.strxor import strxor_c

src = b"1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

src = binascii.unhexlify(src)

keys = []
for key in range(0, 255):
    keys.append(key)
answers = []
for key in keys:
    answer = strxor_c(src, key)
    print(key, answer)
