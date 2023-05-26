#%%
import math
from typing import Tuple


def calc_pythagoras(a:float, 
                    b:float, 
                    rounding:int=1, 
                    double:int=1) -> Tuple[float, float]:
    '''
    Function to apply the pythagoras theorem

    parameters:
    * a
    * b

    returns:
    * c, c_sqrd
    '''
    
    # check the input data types
    required_types = (int, float)

    if type(a) not in required_types:
        raise TypeError(f"The value {a} should be numeric. Got {type(5)}")


    if rounding < 1:
        raise ValueError(f"The rounding value should be higher than 1. Got {rounding}")

    c_sqrd = math.pow(a, 2) + math.pow(b, 2)
    c = math.sqrt(c_sqrd)
    c_rounded = round(c, rounding) * double
    return c_rounded, c_sqrd


#%%
my_c, my_c_sqr = calc_pythagoras(a=5, 
                       b=20,
                       rounding=1,
                       double=2)
print(my_c)

# %%
