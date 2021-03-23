import sys

class Crypt:
    def __init__(self,key):
        self.key = key

    def encrypt(self,msg):
        key = self.key
        msglist = list(msg)
        
        msglen = len(msg)
        ciphertext = [''] * msglen
        for i in range(msglen):
            if ord(msglist[i])>=65 and ord(msglist[i]) <=90:
                flag=True
            else:
                flag=False    
            ciphertext[i] = chr(ord(msglist[i])+int(key))


            if flag == True:
                if (ord(ciphertext[i])>90):
                 ciphertext[i]=chr(ord(ciphertext[i])-26)    
            else:
                 if (ord(ciphertext[i])>122):
                     ciphertext[i]=chr(ord(ciphertext[i])-26)       
        return ''.join(ciphertext)

    def decrypt(self,msg):
        key = self.key
        msglist = list(msg)
        
        msglen = len(msg)
        ciphertext = [''] * msglen
        for i in range(msglen):
            if ord(msglist[i])>=65 and ord(msglist[i]) <=90:
                flag=True
            else:
                flag=False    
            ciphertext[i] = chr(ord(msglist[i])-int(key))


            if flag == True:
                if (ord(ciphertext[i])<65):
                 ciphertext[i]=chr(ord(ciphertext[i])+26)    
            else:
                 if (ord(ciphertext[i])<97):
                     ciphertext[i]=chr(ord(ciphertext[i])+26)       
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