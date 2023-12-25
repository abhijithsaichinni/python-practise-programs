#a boy and his father, a computer programmer, are playing with wooden blocks. They are building a pyramid.
#Their pyramid is a bit weird, as it is actually a pyramid-shaped wall – it's flat. The pyramid is stacked according to one simple principle: each lower layer contains one block more than the layer above.
#Your task is to write a program which reads the number of blocks the builders have, and outputs the height of the pyramid that can be built using these blocks.
#Note: the height is measured by the number of fully completed layers – if the builders don't have a sufficient number of blocks and cannot complete the next layer, they finish their work immediately.


blocks = int(input("Enter the number of blocks: "))

for n in range(blocks): 
    if n*(n+1)/2 <= blocks: 
        height = n

print("The height of the pyramid:", height)


#A pyramid of height N has 1 + 2 + … + N blocks in it. This reduces to N * (N + 1) / 2. So you need to find the largest integer of the form (N^2 + N) / 2 that is less than or equal to your chosen number blocks
