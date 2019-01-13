def twice_as_large(num1, num2):
  if num1 > num2 * 2:
    return True
  return False

print(twice_as_large(5, 10))
# should print False
print(twice_as_large(11, 5))
# should print True