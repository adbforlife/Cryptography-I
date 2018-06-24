from Crypto.Cipher import AES
from binascii import *
import urllib2
import sys

TARGET = 'http://crypto-class.appspot.com/po?er='
#--------------------------------------------------------------
# padding oracle
#--------------------------------------------------------------
class PaddingOracle(object):
    def query(self, q):
        target = TARGET + urllib2.quote(q)    # Create query URL
        req = urllib2.Request(target)         # Send HTTP request to server
        try:
            f = urllib2.urlopen(req)          # Wait for response
        except urllib2.HTTPError, e:
        	return e.code          

if __name__ == "__main__":
	block1 = [84, 104, 101, 32, 77, 97, 103, 105, 99, 32, 87, 111, 114, 100, 115, 32]
	block2 = [97, 114, 101, 32, 83, 113, 117, 101, 97, 109, 105, 115, 104, 32, 79, 115]
	block3 = [115, 105, 102, 114, 97, 103, 101, 9, 9, 9, 9, 9, 9, 9, 9, 9]
	c = "f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4"
	iv = c[:32]
	iv_bytes = [ord(char) for char in unhexlify(iv)]
	c1 = c[32:64]
	c1_bytes = [ord(char) for char in unhexlify(c1)]
	c2 = c[64:96]
	c2_bytes = [ord(char) for char in unhexlify(c2)]
	c3 = c[96:128]
	c3_bytes = [ord(char) for char in unhexlify(c3)]

	print(''.join([chr(char) for char in block1 + block2 + block3]))

	po = PaddingOracle()
	correct_bytes_reversed = [9,9,9,9,9,9,9,9,9]
	for i in range(9,16):
		iv_guess_bytes = []
		for char in unhexlify(c2):
			iv_guess_bytes.append(ord(char))
		for b in range(len(correct_bytes_reversed)):
			iv_guess_bytes[15-b] = iv_guess_bytes[15-b] ^ correct_bytes_reversed[b] ^ (i+1)
		#print(iv_guess_bytes)
		#correct_bytes_reversed.append(1)
		for guess in range(256):
			iv_guess_bytes[15-i] = guess
			c_guess = iv + c1 + ''.join('{:02x}'.format(a) for a in iv_guess_bytes) + c3
			result = po.query(c_guess)
			print(c_guess)
			print(result)
			if result == 403:
				print("fuck" + str(guess))
			elif result == 404:
				correct_byte = guess ^ c2_bytes[15-i] ^ (i+1)
				correct_bytes_reversed.append(correct_byte)
				print(list(reversed(correct_bytes_reversed)))
				break
			else:
				continue

		

			#print('{:02x}'.format(guess))
	#po.query(sys.argv[1])       # Issue HTTP query with the given argument