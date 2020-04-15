def is_palindrome(my_string):
  while len(my_string) > 1:
    if my_string[0] != my_string[-1]:
      return False
    my_string = my_string[1:-1]
  return True

def is_palindrome(my_string):
  if len(my_string)<2:
    return True
  
  else:
    if(my_string[0] != my_string[-1]):
      return False
  return is_palindrome(my_string[1:-1])
  
