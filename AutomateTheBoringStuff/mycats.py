# a program to take in and store values in a string

myCats = []
while True :
    catname = input("Enter the name of cat" + str(len(myCats) + 1) + ' (Or enter nothing to stop.): ')
    if catname == '':
        break 
    else:
        myCats= myCats + [catname]
print('The cat names are:')
for i in myCats:
    print(''+ i)