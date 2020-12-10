import os as random
import base64
import time
class Secure(object):
    def __init__(self):
        self.ASCII_code=[88, 206, 233, 107, 96, 70, 89, 114, 171, 205, 117, 242, 102, 140, 173, 115, 221, 95, 190, 200, 118, 249, 229, 93, 41, 228, 32, 77, 236, 199, 243, 8, 160, 183, 109, 30, 245, 51, 16, 54, 63, 150, 172, 132, 61, 100, 247, 157, 19, 104, 165, 226, 55, 218, 126, 230, 251, 201, 9, 34, 124, 186, 204, 74, 122, 36, 246, 198, 0, 120, 136, 110, 106, 18, 123, 78, 194, 116, 46, 68, 219, 1, 188, 130, 128, 72, 37, 237, 163, 20, 125, 211, 168, 85, 12, 177, 227, 184, 43, 155, 76, 57, 170, 27, 192, 127, 207, 13, 21, 56, 166, 17, 238, 23, 29, 6, 83, 213, 69, 108, 113, 176, 159, 187, 248, 255, 14, 99, 119, 161, 191, 250, 86, 33, 105, 47, 178, 158, 162, 28, 195, 98, 58, 101, 35, 138, 87, 216, 203, 44, 22, 2, 224, 241, 39, 82, 80, 225, 151, 210, 79, 141, 4, 154, 75, 60, 3, 94, 214, 133, 175, 31, 112, 180, 7, 48, 208, 15, 131, 235, 153, 181, 11, 59, 254, 145, 167, 144, 232, 40, 73, 65, 202, 146, 62, 252, 234, 81, 135, 103, 143, 169, 137, 189, 182, 10, 244, 193, 64, 67, 174, 215, 156, 149, 197, 38, 66, 209, 84, 24, 212, 5, 152, 90, 148, 129, 42, 164, 239, 49, 92, 139, 45, 121, 134, 142, 97, 240, 52, 25, 196, 26, 220, 222, 223, 147, 111, 185, 91, 253, 231, 71, 53, 179, 50, 217]
        self.enc=[40, 64, 60, 88, 42, 97, 109, 108, 121, 103, 36, 95, 43, 104, 106, 122, 58, 62, 124, 102, 120, 113, 101, 37, 112, 54, 117, 57, 98, 93, 51, 61, 111, 99, 63, 53, 100, 116, 33, 96, 107, 119, 49, 41, 91, 48, 105, 118, 50, 114, 52, 115, 55, 125, 94, 126, 110, 46, 44, 56, 35, 69, 123, 66]
        self.key=""
        self.enckey=""
    def encrypt(self,data,key):
        temp=""
        i=0
        self.enckey = key
        if self.enckey == "":
            self.generate_key()    
        data=data+self.enckey
        while(i<len(data)):
                n=self.ASCII_code.index(data[i])
                n=bin(n)[2:]
                n=n.zfill(8)
                temp=temp+n
                i+=1
        i=0
        cliper=""
        while i<len(temp):
            n=temp[i:i+6]
            i+=6
            n=int(n,2)
            n=self.enc[n]
            n=chr(n)
            cliper=cliper + n
        return cliper
    def decrypt(self,data,key):
        temp=list(data)
        i=0
        total=len(data)
        while(i<total):
            # print(data[i],end="")
            n=self.enc.index(data[i])
            n=bin(n)[2:]
            if i == total-1 :
                n=n.zfill(6-(6*total%8))
            else:
                n=n.zfill(6)
            # print(int(n,2),end=" ")
            temp[i]=n
            i+=1
        i=0
        ori=[]
        temp="".join(temp)
        self.verify_key(key,temp[-192:])
        while i < (len(temp)-192):
            n=temp[i:i+8]
            i+=8
            n=int(n,2)
            n=self.ASCII_code[n]
            if n == 13:
                continue
            n=chr(n)
            ori.append(n)
        ori="".join(ori)
        return ori
    def generate_key(self):
        self.enckey=base64.urlsafe_b64encode(random.urandom(16))
        return self.enckey
    def verify_key(self,k,data): 
        self.key=""
        i=0
        while i<len(data):
            n=data[i:i+8]
            i+=8
            n=int(n,2)
            n=self.ASCII_code[n]
            n=chr(n)
            self.key=self.key+n
        if self.key != k:
            print("Key Does Not Match")
            time.sleep(3)
            raise "Invalid Token"
def encrypt_msg(msg,key):
    a=Secure()
    #print(msg)
    return a.encrypt(msg,key)
def decrypt_msg(msg,key):
    a=Secure()
    #print(msg)
    return a.decrypt(msg,key)
def get_key():
    a=Secure()
    return(a.generate_key())
