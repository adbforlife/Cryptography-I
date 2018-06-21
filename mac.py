from Crypto.Hash import SHA256
from binascii import *

strings = []

with open("/Users/ADB/Desktop/6.1.intro.mp4", "r") as f:
	while True:
		s = f.read(1024)
		if not s:
			break
		strings.append(s)

h = ""
for s in reversed(strings):
	h = SHA256.new(s + h).digest()
print(hexlify(h))