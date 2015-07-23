from Crypto.Util.strxor import strxor_c
import binascii

files = []
keys = []
unhex = []

freqs = {
    'a': 0.0651738,
    'b': 0.0124248,
    'c': 0.0217339,
    'd': 0.0349835,
    'e': 0.1041442,
    'f': 0.0197881,
    'g': 0.0158610,
    'h': 0.0492888,
    'i': 0.0558094,
    'j': 0.0009033,
    'k': 0.0050529,
    'l': 0.0331490,
    'm': 0.0202124,
    'n': 0.0564513,
    'o': 0.0596302,
    'p': 0.0137645,
    'q': 0.0008606,
    'r': 0.0497563,
    's': 0.0515760,
    't': 0.0729357,
    'u': 0.0225134,
    'v': 0.0082903,
    'w': 0.0171272,
    'x': 0.0013692,
    'y': 0.0145984,
    'z': 0.0007836,
    ' ': 0.1918182
}
keys = []
scores = {}
for key in range(0, 100):
    keys.append(key)

def score(answer):
    scr = 0
    for i in answer:
        c = chr(i).lower()
        if c in freqs:
            scr += freqs[c]
    return scr

with open('/Users/amandaclark/PycharmProjects/CryptoChallenge/Set 1/data') as f:
    for line in f:
        files.append(line.rstrip('\n').encode('UTF-8'))

for string in files:
    unhex.append(binascii.unhexlify(string))

for encrypt in unhex:
    for key in keys:
        answer = strxor_c(encrypt, key)
        scr = score(answer)
        scores[scr] = encrypt


foo = max(scores, key = scores.get)
print(foo, scores[foo])



