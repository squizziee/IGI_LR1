import os

import circle
import square

side = float(os.environ['SIDE'])
radius = float(os.environ['RADIUS'])

print(f'Circle area : {circle.area(radius)}')
print(f'Square area : {square.area(side)}')
print(f'Circle area : {circle.perimeter(radius)}')
print(f'Square area : {square.perimeter(side)}')
