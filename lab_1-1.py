# Azaan Dawson

total = 0
while True:
  user_input = int(input("Enter a number "))   
  if user_input != -1 :
    total += user_input
  else:
    break
print(("The sum of all the numbers entered is {0}" ).format(total)) 
