import derivative
def sqrt(num):
  guess = .5*num
  function = "x^2"
  fderiv = derivative.derive(function).replace('x',"")

  number = num
  for i in range(1000):
    n1 = (guess*guess-number)
    n2 = (int(fderiv)*guess)
    n = guess - (n1/n2)
    guess = n
  return guess
for i in range(1,1001):
  print(sqrt(i))
