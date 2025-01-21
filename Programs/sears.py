billThickness = 1.1 * 10**-4
towerHeight = 442 # meters

numBills = 1
days = 1

while numBills * billThickness < towerHeight:
    print("Day:", days, "Bills", numBills, "Height", numBills * billThickness)
    days = days + 1
    numBills = numBills * 2

print("It took ", days, "days to be taller than sears tower at a height of ", round(numBills * billThickness))