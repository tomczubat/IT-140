import sys


# Get the rental code from the customer
rentalCode = input('(B)udget, (D)aily, or (W)eekly rental?\n')


# Get the rental period from the customer
if rentalCode == 'B':
  rentalPeriod = int(input('Number of Days Rented:\n'))
elif rentalCode == 'D':
  rentalPeriod = int(input('Number of Days Rented:\n'))
else:
  rentalPeriod = input('Number of Weeks Rented:\n')

# Set the charges depending on the rental code
budgetCharge = int(40.00)
dailyCharge = int(60.00)
weeklyCharge = int(190.00)

# Calculate the base charge depending on the rental code
if rentalCode == "B":
  baseCharge = rentalPeriod * 40.00
elif rentalCode == "D":
  baseCharge = rentalPeriod * 60.00
else:
  baseCharge = rentalPeriod * 190.00


# Get the starting milage from the customer 
odoStart = input('Starting Odometer Reading:\n')
# Get the ending milage from the customer
odoEnd = input('Ending Odometer Reading:\n')

# Calculate total milage
totalMiles = int(odoEnd) - int(odoStart)

# Calculate average day miles
averageDayMiles = totalMiles / rentalPeriod

# Calculate the base charge
if rentalCode == 'B':
  mileCharge = totalMiles * 0.25
elif rentalCode == 'D' and averageDayMiles < 100:
  mileCharge = 0
elif rentalCode == 'D' and averageDayMiles > 100:
  extraMiles = averageDayMiles - 100
  mileCharge = extraMiles * 0.25
elif rentalCode == 'W' and averageDayMiles > 900:
  mileCharge = weeksRented * 100.00
else:
  mileCharge = 0

# Print out the summary
amtDue = float(baseCharge) +float(mileCharge)
amtDue = format(amtDue, '.2f')
print('Rental Summary')
print('Rental Code:       ' + rentalCode)
print('Rental Period:     ' + str(rentalPeriod))
print('Starting Odometer: ' + odoStart)
print('Ending Odometer:   ' + odoEnd)
print('Miles Driven:      ' + str(totalMiles))
print('Amount Due:       $' + amtDue )


