from binascii import *
target_str = "0x32510ba9babebbbefd001547a810e67149caee11d945cd7fc81a05e9f85aac650e9052ba6a8cd8257bf14d13e6f0a803b54fde9e77472dbff89d71b57bddef121336cb85ccb8f3315f4b52e301d16e9f52f904"
target = int(target_str, 16)
c1 = 0x315c4eeaa8b5f8aaf9174145bf43e1784b8fa00dc71d885a804e5ee9fa40b16349c146fb778cdf2d3aff021dfff5b403b510d0d0455468aeb98622b137dae857553ccd8883a7bc37520e06e515d22c954eba50
c2 = 0x234c02ecbbfbafa3ed18510abd11fa724fcda2018a1a8342cf064bbde548b12b07df44ba7191d9606ef4081ffde5ad46a5069d9f7f543bedb9c861bf29c7e205132eda9382b0bc2c5c4b45f919cf3a9f1cb741
c3 = 0x32510ba9a7b2bba9b8005d43a304b5714cc0bb0c8a34884dd91304b8ad40b62b07df44ba6e9d8a2368e51d04e0e7b207b70b9b8261112bacb6c866a232dfe257527dc29398f5f3251a0d47e503c66e935de812
c4 = 0x32510ba9aab2a8a4fd06414fb517b5605cc0aa0dc91a8908c2064ba8ad5ea06a029056f47a8ad3306ef5021eafe1ac01a81197847a5c68a1b78769a37bc8f4575432c198ccb4ef63590256e305cd3a9544ee41
secret = ['_' for i in range((len(target_str) - 2) // 2)]
m1 = ['_' for i in range((len(target_str) - 2) // 2)]
m2 = ['_' for i in range((len(target_str) - 2) // 2)]
m3 = ['_' for i in range((len(target_str) - 2) // 2)]
m4 = ['_' for i in range((len(target_str) - 2) // 2)]

alph = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
freq = [0 for i in range(128)]

for i in alph:
	pos = ord(i) ^ ord(' ')
	freq[pos] = 2

for i in alph:
	for j in alph:
		pos = ord(i) ^ ord(j)
		freq[pos] = 1

#for i in range(len(freq)):
	#print(i, freq[i])
xor1 = hex(target ^ c1)[:-1]
xor2 = hex(target ^ c2)[:-1]
xor3 = hex(target ^ c3)[:-1]
xor4 = hex(target ^ c4)[:-1]
if len(target_str) > len(xor1):
	xor1 = xor1[:2] + (len(target_str) - len(xor1)) * "0" + xor1[2:]
if len(target_str) > len(xor2):
	xor2 = xor2[:2] + (len(target_str) - len(xor2)) * "0" + xor2[2:]
if len(target_str) > len(xor3):
	xor3 = xor3[:2] + (len(target_str) - len(xor3)) * "0" + xor3[2:]
if len(target_str) > len(xor4):
	xor4 = xor4[:2] + (len(target_str) - len(xor4)) * "0" + xor4[2:]

target_str = target_str[2:]
xor1 = xor1[2:]
xor2 = xor2[2:]
xor3 = xor3[2:]
xor4 = xor4[2:]
target_list = []
xor1_list = []
xor2_list = []
xor3_list = []
xor4_list = []
c1_str = hex(c1)[2:-1]
c2_str = hex(c2)[2:-1]
c3_str = hex(c3)[2:-1]
c4_str = hex(c4)[2:-1]
list1 = []
list2 = []
list3 = []
list4 = []

for i in range(len(target_str)):
	if i % 2 == 0:
		target_list.append(int(target_str[i:i+2], 16))
		xor1_list.append(int(xor1[i:i+2], 16))
		xor2_list.append(int(xor2[i:i+2], 16))
		xor3_list.append(int(xor3[i:i+2], 16))
		xor4_list.append(int(xor4[i:i+2], 16))
		list1.append(int(c1_str[i:i+2], 16))
		list2.append(int(c2_str[i:i+2], 16))
		list3.append(int(c3_str[i:i+2], 16))
		list4.append(int(c4_str[i:i+2], 16))

for i in range(len(target_list)):
	if xor1_list[i] >= 64 and xor2_list[i] >= 64 and xor3_list[i] >= 64 and xor4_list[i] >= 64:
		secret[i] = ' '
		m1[i] = chr(32 ^ xor1_list[i])
		m2[i] = chr(32 ^ xor2_list[i])
		m3[i] = chr(32 ^ xor3_list[i])
		m4[i] = chr(32 ^ xor4_list[i])
	elif xor1_list[i] >= 64:
		m1[i] = ' '
		secret[i] = chr(32 ^ xor1_list[i])
	elif xor2_list[i] >= 64:
		m2[i] = ' '
		secret[i] = chr(32 ^ xor2_list[i])
	elif xor3_list[i] >= 64:
		m3[i] = ' '
		secret[i] = chr(32 ^ xor3_list[i])
	elif xor4_list[i] >= 64:
		m4[i] = ' '
		secret[i] = chr(32 ^ xor4_list[i])

guess = "The secret message is: When using a stream cipher, never use the key more than once"
guess1 = "We can factor the number 15 with quantum computers. We can also factor the number 1"
guess2 = "Euler would probably enjoy that now his theorem becomes a corner stone of crypto - "
guess3 = "The nice thing about Keeyloq is now we cryptographers can drive a lot of fancy cars"
guess4 = "The ciphertext produced by a weak encryption algorithm looks as good as ciphertext "
#guess = guess + (len(secret) - len(guess)) * "_"
for i in range(len(guess)):
	m1[i] = chr(xor1_list[i] ^ ord(guess[i]))
	m2[i] = chr(xor2_list[i] ^ ord(guess[i]))
	m3[i] = chr(xor3_list[i] ^ ord(guess[i]))
	m4[i] = chr(xor4_list[i] ^ ord(guess[i]))
for i in range(len(guess1)):
	secret[i] = chr(xor1_list[i] ^ ord(guess1[i]))
	m2[i] = chr(list1[i] ^ list2[i] ^ ord(guess1[i]))
	m3[i] = chr(list1[i] ^ list3[i] ^ ord(guess1[i]))
	m4[i] = chr(list1[i] ^ list4[i] ^ ord(guess1[i]))
for i in range(len(guess2)):
	secret[i] = chr(xor2_list[i] ^ ord(guess2[i]))
	m1[i] = chr(list2[i] ^ list1[i] ^ ord(guess2[i]))
	m3[i] = chr(list2[i] ^ list3[i] ^ ord(guess2[i]))
	m4[i] = chr(list2[i] ^ list4[i] ^ ord(guess2[i]))
for i in range(len(guess3)):
	secret[i] = chr(xor3_list[i] ^ ord(guess3[i]))
	m1[i] = chr(list3[i] ^ list1[i] ^ ord(guess3[i]))
	m2[i] = chr(list3[i] ^ list2[i] ^ ord(guess3[i]))
	m4[i] = chr(list3[i] ^ list4[i] ^ ord(guess3[i]))
for i in range(len(guess4)):
	secret[i] = chr(xor4_list[i] ^ ord(guess4[i]))
	m1[i] = chr(list4[i] ^ list1[i] ^ ord(guess4[i]))
	m2[i] = chr(list4[i] ^ list2[i] ^ ord(guess4[i]))
	m3[i] = chr(list4[i] ^ list3[i] ^ ord(guess4[i]))

print("".join(secret))
print("".join(m1))
print("".join(m2))
print("".join(m3))
print("".join(m4))









