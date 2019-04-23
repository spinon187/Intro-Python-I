x = int(input('Enter number: '))

for i in range(1, x+1):
  if i != x and i != 1:
    if x % i == 0:
      print('The number is not prime')
      break
  elif i == x:
    print('The number is prime')