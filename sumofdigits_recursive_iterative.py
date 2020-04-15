def sum_digits(n):
  if n < 0:
    ValueError("Inputs 0 or greater only!")
  result = 0
  while n is not 0:
    result += n % 10
    n = n // 10
  return result + n
  
  def sum_digits(n):
  if n<=9:
    return n
  else:
    return sum_digits(n//10)+n%10 
