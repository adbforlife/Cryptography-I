from Crypto.Cipher import AES
from Crypto.Util import Counter
from binascii import *

cbc_key = "140b41b22a29beb4061bda66b6747e14"
cbc_c1 = "4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81"
cbc_c2 = "5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253"
ctr_key = "36f18357be4dbd77f050515c73fcf9f2"
ctr_c1 = "69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329"
ctr_c2 = "770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451"
cbc_iv1 = cbc_c1[:32]
cbc_c1 = cbc_c1[32:]
cbc_iv2 = cbc_c2[:32]
cbc_c2 = cbc_c2[32:]
ctr_iv1 = ctr_c1[:32]
ctr_c1 = ctr_c1[32:]
ctr_iv2 = ctr_c2[:32]
ctr_c2 = ctr_c2[32:]

ctr1 = Counter.new(128, initial_value=int(ctr_iv1, 16))
ctr2 = Counter.new(128, initial_value=int(ctr_iv2, 16))

cbc_obj1 = AES.new(unhexlify(cbc_key), AES.MODE_CBC, unhexlify(cbc_iv1))
cbc_m1 = cbc_obj1.decrypt(unhexlify(cbc_c1))
print(cbc_m1)
cbc_obj2 = AES.new(unhexlify(cbc_key), AES.MODE_CBC, unhexlify(cbc_iv2))
cbc_m2 = cbc_obj2.decrypt(unhexlify(cbc_c2))
print(cbc_m2)
ctr_obj1 = AES.new(unhexlify(ctr_key), AES.MODE_CTR, counter=ctr1)
ctr_m1 = ctr_obj1.decrypt(unhexlify(ctr_c1))
print(ctr_m1)
ctr_obj2 = AES.new(unhexlify(ctr_key), AES.MODE_CTR, counter=ctr2)
ctr_m2 = ctr_obj2.decrypt(unhexlify(ctr_c2))
print(ctr_m2)