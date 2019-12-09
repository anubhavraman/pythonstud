ar=int(input("Feed me with num:"))
cmn=0
i=2
while i<=ar:
    if ar%i==0:
        cmn=cmn+1
        break
    i=i+1
if cmn==0 and ar!=1:
    print("Prime",ar)
else:
    print("Non-Pime",ar)