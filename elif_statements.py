def grade_converter(gpa):
  grade = "F"
  if gpa >= 4.0:
    return "A"
  elif gpa >= 3.0:
    return "B"
  elif gpa >= 2.0:
    return "C"
  elif gpa >= 1.0:
    return "D"
  elif gpa >=0.0:
    return "F"
  return grade
print(grade_converter(3.854))