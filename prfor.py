ar=int(input("Feed me with num:"))
cmn=0
for i in range(2, ar+1):
    if ar%i == 0:
        cmn = cmn+1
        break
if cmn==0 and ar!=1:
    print("Prime",ar)
else:
    print("Non-Pime",ar)