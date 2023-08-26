numneed = int(input("What positive number do you wish to find the sum of positive even numbers for?\n"))
total = 0 
for number in range(2,numneed + 2,2):
    total += number
print(total)