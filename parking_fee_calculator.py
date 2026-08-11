hours = int(input("Enter parking hours: "))

if hours <= 2:
    charge = hours * 30
elif hours <= 5:
    charge = hours * 25
else:
    charge = hours * 20

if charge > 150:
    service_charge = 20
else:
    service_charge = 0

final_amount = charge + service_charge

print("Parking Charge: ₹", charge)
print("Service Charge: ₹", service_charge)
print("Final Amount: ₹", final_amount)