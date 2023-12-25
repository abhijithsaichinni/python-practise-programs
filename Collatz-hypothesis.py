num=int(input("Enter a number: "))
i=0

if (num <= 0):
    print("Invalid Input")
else:
    while num !=1:
        if(num%2==0):
            num=num/2
        else:
            num=3*num+1
        print(int(num))
        i+=1
print("steps: ", i)
