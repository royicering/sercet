import sys

class Crypt:
    def __init__(self,key):
        self.key = key

    def encrypt(self,msg):
        keylist = list(self.key)
        msglist = list(msg)
        keylen = len(keylist)
        msglen = len(msg)
        ciphertext = [''] * msglen
        for i in range(msglen):
            ciphertext[i] = chr(ord(msglist[i]) ^ ord(keylist[i % keylen]))
        return ''.join(ciphertext)

    def dencrypt(self,msg):
        keylist = list(self.key)
        msglist = list(msg)
        keylen = len(keylist)
        msglen = len(msg)
        ciphertext = [''] * msglen
        for i in range(msglen):
            ciphertext[i] = chr(ord(msglist[i]) ^ ord(keylist[i % keylen]))
        return ''.join(ciphertext)

if __name__ == "__main__":

    print(sys.argv)
    if len(sys.argv) > 2:
        if sys.argv[1] == '-e':
            c = Crypt(sys.argv[2])
            print(c.encrypt(sys.argv[3]))
        elif sys.argv[1] == '-d':
            c = Crypt(sys.argv[2])
            print(c.decrypt(sys.argv[3]))