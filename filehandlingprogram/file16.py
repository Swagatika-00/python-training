#write a list in file using binary format
import pickle
numbers=[10,20,30,40,50]
f=open("xyz.dat","wb")#wb write binary
pickle.dump(numbers,f)    #store list in binary file
f.close()