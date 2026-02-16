for i in range(1,11):
    if i==5:            #5 will not be printed in case of break 1,2,3,4 will be printed
        continue
    print(i)
print("End of the program")

i=1
while i<10:
    if i==5:
        break
    print(i)
    i+=1

i=1
while i<10:
    if i==5:
        continue
    print(i)
    i+=1