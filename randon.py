import random
import PySimpleGUI

lower = int(input("enter lower 1bound "))
upper = int(input("enter upper bound "))
result = random.randrange(lower, upper+1)
print(result)