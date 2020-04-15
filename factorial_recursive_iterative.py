# Recursive
def factorial(n):  
  if n < 0:    
    ValueError("Inputs 0 or greater only") 
  if n <= 1:    
    return 1  
  return n * factorial(n - 1)
  
  # iterative
  def factorial(n):
  if n<=1:
    return 1
  result=1
  for i in range(1,n+1):
    result=result*i
  return result 
