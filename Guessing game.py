import random
y=random.randint(0,100)
print ("Guess a number between 0 and 100 (included). You will get hints if you are far or close to the correct number.")
print ("If your guess is within 10 numbers, I will tell you HEAT, if not I will tell you COLD.")
print ("If your guess is farther than your most recent guess, I'll say you're getting COLDER") 
print ("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
l=[0]
while True:
    x=int(input("Enter a number between 0 and 100: "))
    if x<0 or x>100:
        print("OUT OF BOUNDS")
        continue
    if x==y:
        print ('CONGRATULATIONS, YOU GUESSED IT IN ONLY' + " " +str(len(l))+ " "+ 'GUESSES!!')
        break
    
    l.append(x)
    
    if l[-2]:
        if abs(x-y)<abs(x-l[-2]):
            print ("WARMER")
        else:
            print ("COLDER")
    else:
        if abs(x-y)<=10:
            print ("WARM")
        else:
            print ("COLD")
