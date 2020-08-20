# the function below takes in a complex number as a string with j as the indicated variable for the complex number and prints the r and theta of the polar coordinate

import math, cmath

def complex_parts(complex_num_list):
    # checks for img != 0
    if 'j' in complex_num_list:
        for x in range(2,len(complex_num_list)+1):
            # looks for + or - then captures imaginary
            if not complex_num_list[-x].isdigit():
                img = int(''.join(complex_num_list[-x:-1]))
                try:
                    real = int(''.join(complex_num_list[:-x]))
                except ValueError:
                    real = 0
                break
        
        return [real, img]
        
        # No + or - found (must be only imaginary)
        img = int(''.join(complex_num_list[:-1]))
        return [0, img]
    # only real part
    else:
        real = int(''.join(complex_num_list))
        img = 0
        return [real, img]

parts = complex_parts(list('2+5j'))
print(abs(complex(parts[0],parts[1])))
print(cmath.phase(complex(parts[0],parts[1])))
