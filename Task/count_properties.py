s=input("enter string:")
al,nm,uc,lc,sp=0,0,0,0,0
for i in s:
    if i.isalpha():
        a1=a1+1
    elif i.isnumeric():
         nm=nm+1
    elif i.isspace():
     sp=sp+1
    if i.isupper():
       uc=uc+1
    elif i.islower():
     lc=lc+1
     print("number of alphabets:",al)
     print("number of numericals:",nm)
     print("number of space:",sp)
     print("number of uppercase:",uc)
     print("number of lowercase:",lc)
                        
