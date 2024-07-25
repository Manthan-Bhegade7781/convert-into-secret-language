st=input("Enter a character:")
nwords=st.split(" ")
coding=input("enter option(coding/decoding):")
if(coding=="coding"):
    r1="bdud"
    r2="gfej"
    words=[]
    for word in nwords:
        if(len(word)>=3):
            newst=r1+word[1:]+word[0]+r2
            words.append(newst)
        else:
            words.append(word[::-1])
    print(" ".join(words))

else:
    
    words=[]
    for word in nwords:
        if(len(word)>=3):
            newst=word[4:-4]
            newst=newst[-1]+newst[:-1]
            words.append(newst)
        else:
            words.append(word[::-1])
    print(" ".join(words))
