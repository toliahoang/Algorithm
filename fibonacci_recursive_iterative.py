# Recursive
def fibonacci(n):
  if n < 0:
    ValueError("Input 0 or greater only!")
  if n <= 1:
    return n
  return fibonacci(n - 1) + fibonacci(n - 2)
  
# Iterative
def fibonacci(n):
  if n==0:
    return n
  a,b=0,1 
  count=0
  c=0
  while (count <=n-2):
    c=a+b
    a=b
    b=c
 
    
    #a,b=b,a+b
    count=count+1
    #print(count)
    #print('c',c)
  return c
