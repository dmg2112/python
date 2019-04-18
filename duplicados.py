Nums=[1,1,2,3,2,2,2,1,1,4,4,1]
longitud = len(Nums)
depur = []

for n in range(longitud):
    actual= Nums[n]
    leng2= len(depur)-1
    if(len(depur)>0):
        ultimo = depur[-1]
    else:
        ultimo=0
    if(longitud == 0):
        depur.append(actual)
    elif(longitud==(len(Nums)-1)):
        if(ultimo!=actual):
            depur.append(actual)
    else:
        
        if(ultimo!=actual):
            depur.append(actual)
    
 

print(depur)





