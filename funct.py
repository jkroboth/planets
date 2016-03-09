## CREATING FUNCTIONS ##
def fahr_to_kelvin(temp):
  return ((temp-32)*(5/9) + 273.15)

print("Freezing point of water:", fahr_to_kelvin(32))
print("Boiling point of water:", fahr_to_kelvin(212))

def kelvin_to_celcius(temp_k):
  return temp_k -273.15

print("Absolute zero in Celcius", kelvin_to_celcius(273))

def fahr_to_celcius(temp_f):
  temp_k = fahr_to_kelvin(temp_f)
  result = kelvin_to_celcius(temp_k)
  return result

print("Freezing point of water", fahr_to_celcius(32.0))
