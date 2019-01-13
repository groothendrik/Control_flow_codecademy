#this one doesn't work

def ground_shipping(weight):
  premium_ground_shipping = 105.0
  if weight <= 2.0:
    return weight * 1.50 + 20
  elif weight <= 6.0:
    return weight *3.0 + 20
  elif weight <= 10.0:
    return weight * 4 + 20
  else:
    return weight * 4.75 + 20

#print(ground_shipping(8.4))

def drone_shipping(weight):
  if weight <= 2.0:
    return weight *4.50
  elif weight <= 6:
    return weight * 6.0
  elif weight <= 10.0:
    return weight *12.00
  else:
    return weight * 14.25

#print(drone_shipping(1.5))

def cheapest_shipping(weight):
  ground = ground_shipping(weight)
  premium = ground + premium_ground_shipping
  drone = drone_shipping(weight)
  if ground < premium and ground < drone:
    cost = ground
  elif premium < ground and premium < drone:
    cost = premium
  elif drone < ground and drone < premium:
    cost = drone

