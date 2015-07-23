import binascii

text = bytearray(b"Burning \\'em, if you ain\\'t quick and nimble\
# I go crazy when I hear a cymbal")
key = bytearray(b"ICE")
answer = bytearray(len(text))

for i in range(len(text)):
    answer[i] = text[i] ^ key[i % len(key)]

answer = binascii.hexlify(answer)
print(answer)


