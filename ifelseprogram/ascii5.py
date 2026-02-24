import sys
print("enter a char")
ch=input()
if len(ch) >1:
   print("one char allow")
   sys.exit()
ch=ord(ch)
if ch>=65 and ch<=90:
ch=chr(ch+32)
   print(ch)   