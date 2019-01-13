def always_false(num):
  if num <= -1 and num >= 0:
    return False


print(always_false(0))
# should print False
print(always_false(-1))
# should print False
print(always_false(1))
# should print False