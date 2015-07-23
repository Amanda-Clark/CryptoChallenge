import binascii
str1 = binascii.unhexlify(b'1c0111001f010100061a024b53535009181c')
str2 = binascii.unhexlify(b'686974207468652062756c6c277320657965')

ans = ''.join(chr((a) ^ (b)) for a, b in zip(str1, str2))
print(ans)
