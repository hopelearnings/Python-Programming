
import sys

try:
    x = int(input('X: '))
    y = int(input('Y: '))
except ValueError:
   print("Error: Please enter a number")
   sys.exit(1)



try:
  result = x / y
  print(f"{x} / {y} = {result}")
except ZeroDivisionError:
  print("Error: cannot devide a number by Zero")
  sys.exit(1)






