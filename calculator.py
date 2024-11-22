def addition(a,b):
 ouput=a + b
 return ouput

def subtraction(a, b):
  output=a-b 
  return output

def multiplication(a,b):
  output=a*b
  return output

def division(a,b):
  output= a/b
  if b == 0:
    raise ValueError("Cannot divide by zero.")
  return output

if __name__ == "__main__":
  addition
  subtraction
  multiplication
  division
  
