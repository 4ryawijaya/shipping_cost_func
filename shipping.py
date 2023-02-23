weight = float(input("Enter your item weights:"))
print("Chouse your shipping method: ")


#Ground Shipping
# def ground_shipping():
def ground_shipping(weight): 
  if weight <= 2:
    charge = weight * 1.50 + 20
  elif weight <= 6:
    charge = weight * 3.00 + 20
  elif weight <= 10:
    charge = weight * 4.00 + 20
  else:
    charge = weight * 4.75 + 20

  print("Cost of ground shipping is", charge)

def premium_shipping():
  premium_charge = 125
  print("Cost of premium charge is", premium_charge)

#Drone Shipping
def drone_shipping(weight):
  if weight <= 2:
    drone_cost = weight * 4.5
  elif weight <= 6:
    drone_cost = weight * 9.0
  elif weight <= 10:
    drone_cost = weight * 12.0
  else:
    drone_cost = weight * 14.25
  print("Your weight is", weight, "The cost for drone shipping is", drone_cost)


