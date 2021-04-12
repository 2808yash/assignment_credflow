import threading 
from threading import*
import time

d={} 
def create(key,value,timeout=0):
    if key in d:
        print("error: this key already exists")
    else:
        if(key.isalpha()):
            if len(d)<(1024*1020*1024) and value<=(16*1024*1024):
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: 
                    d[key]=l
            else:
                print("error: Memory limit exceeded!! ")
        else:
            print("error: Invalind key name i.e. should contain only character value")

def read(key):
    if key not in d:
        print("error: given key does not exist. Please enter a valid key")
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                stri=str(key)+":"+str(b[0]) 
                return stri
            else:
                print("error: ",key," has been expired")
        else:
            stri=str(key)+":"+str(b[0])
            return stri


def delete(key):
    if key not in d:
        print("error: given key does not exist. Please enter a valid key")
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                del d[key]
                print("key deleted successfully")
            else:
                print("error:  ",key,"has been expired")
        else:
            del d[key]
            print("key deleted successfully")
