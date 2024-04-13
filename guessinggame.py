import random

def computerguess(lowval,highval,randnum,count=0):
    if highval>=lowval:
        guess=lowval+(highval-lowval)//2
        if guess == randnum:
            return count
        elif guess>randnum:
            count+=1
            return computerguess(lowval,guess-1,randnum,count)
        else:
            count+=1
            return computerguess(guess+1,highval,randnum,count)
    else:
        #number not found
        return -1
    #end of function

#generate a random number between 1 and 100
randnum=random.randint(1,101)

count = 0
guess = -99
while(guess!=random):
    # get the users guess
    guess = (int)(input("Enter your guess b/w 1 and 100: "))
    if guess<randnum:
        print("higher")
    elif guess>randnum:
        print("lower")
    else:
        print("you guessed it!!")
        break
    count+=1
#end of while loop

print("you took " + str(count)+ " steps to guess the number")
print("computer took " + str(computerguess(0,100,randnum))+" steps!!")
