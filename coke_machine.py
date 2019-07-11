//Coke vending machine. The machine is always on.

while True:
    accepted=[5,10,20,50,100]
    total=0
    print ("Have a Coke! Price: 1.25")
    while total<125:
        print("Insert coin: (5,10,20,50 or 100 only)", end=" ")
        coin= int(input())
        if coin in accepted:
            total+=coin
            print ("Amount entered: ", total, " pence.")
        else:
            print("**Rejecting ", coin, " pence coin.")
    while True:
        print("Make your selection:")
        print("1-Regular Coke")
        print("2-Coke Zero")
        print("3-Caffeine free")
        selection=int(input())
        if selection ==1:
            print("Dispensing Regular Coke")
            break
        elif selection==2:
            print("Dispensing Coke Zero")
            break
        elif selection==3:
            print("Dispensing Caffeine free")
            break
        else: 
            print("** no such beverage")
    if total>125:
        change =total-125
        while change>0:
            if change>=50:
                print("Returning fifty pence")
                change-=50
            elif change>=25:
                print("Returning twenty pence")
                change-=20
            elif change>=10:
                print("Returning ten pence")
                change-=10
            else:
                print("Returning five pence")
                change-=-5


