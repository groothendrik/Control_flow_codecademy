def ground_shipping(weight):
  premium_ground_shipping = 125.0
  if weight <= 2.0:
    price_per_pound = 1.50
  elif weight<= 6.0:
    price_per_pound = 3.0
  elif weight <= 10.0:
    price_per_pound = 4.00
  else:
    price_per_pound = 4.75
  return weight * price_per_pound + 20

#print(ground_shipping(4.8))

def drone_shipping(weight):
  if weight <= 2.0:
    price_per_pound = 4.50
  elif weight<= 6.0:
    price_per_pound = 9.00
  elif weight <= 10.0:
    price_per_pound = 12.00
  else:
    price_per_pound = 14.25
  return weight * price_per_pound

#print(drone_shipping(4.8))

def cheapest_shipping_method(weight):
  ground = ground_shipping(weight)
  premium = 125
  drone = drone_shipping(weight)
  if ground < premium and ground < drone:
    method= "Standard ground shipping"
    cost = ground
  elif premium < ground and premium < drone:
    method = "premium ground  shipping"
    cost = premium
  elif drone < ground and drone < premium:
    method = "drone shipping"
    cost = drone
  print("the package will cost you $" + str(cost) + " and you need to use " + method + " to make it true.")

cheapest_shipping_method(4.8)