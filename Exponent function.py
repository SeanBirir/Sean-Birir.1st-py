"""using for loops to create exponent functions,they allow numbers to be raised to a specific power"""

from unittest import result


def raise_to_power(base_num ,power_num):
    result = 1 
    for index in range(power_num):
        result = result*base_num
    return result

print (raise_to_power(3 ,2))     
