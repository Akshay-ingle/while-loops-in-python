nm=int(input("enter a number:  "))

su=0

temp=nm

while temp>0:
    dt=temp%10
    su+=dt**3
    temp//=10

if nm==su: 
    print(nm,"is an Amstrong number!!")

else:
    print(nm,"is not an Amstrong number!!")    

