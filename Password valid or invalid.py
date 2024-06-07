s=input()
false=''
l,u,d,p=False,False,False,False
for i in s:
    if i.isalpha():
      x=ord(i)
      if x >=97 and x <=122:
        l=True
      else:
        u=True
    elif i.isdigit():
      d=True
    elif i in string.punctuation:
      p=True
if len(s) > 8 and l==True and u==True and d==True and p==True:
  print("valid")
else:
 print("invalid") 
