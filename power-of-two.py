# gives the powe of two until the value entered
of=int(input("Enter the power value:"))
power = 1
for expo in range(of+1):
    print("2 to the power of", expo, "is", power)
    power *= 2
