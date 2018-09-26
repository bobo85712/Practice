import random
key=random.randint(1,100)
G=input('guess a number from 1 to 100:')
guess=int(G)
if guess == key:
     print("Congratulations!")
i = 1
while guess != key and i < 10:
    if guess > key:
         print("too big")
    else: 
         print("too small")
    i += 1
    n1=11-i
    n=str(n1)
    print('You left'+" "+ n +' '+ 'chance, go for it!')
    G=input('You got a wrong number! Guess again:')
    guess=int(G)
    if guess == key:
     print("Congratulations!")
if i==10 and guess != key:
 print("Sorry! you lose the gmae!")
else:
 print("Thank you for playing this")