# Module = a file containing code you want to include in your program
# use 'import' to include a module (built-in or your own)
# useful to break up a large program reusable separate files

# print(help("modules"))

# import math
import math as m

print(m.pi)
from math import pi

print(pi)

import math_module as mm

print(mm.pi)
print(mm.sq(10))
