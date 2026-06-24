units = int(input("Enter the units of electricity consumed."))

if units < 50:
    amount = units*2.60
    surcharge = 25
elif units <= 100:
    amount = (units-50)*3.25
    surcharge = 35
total = amount + surcharge
print("\nElectricity bill is:",total)