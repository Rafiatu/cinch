from random import randint

def generate_otp():
    
    range_start = 10**(6-1)
    range_end = (10**6)-1
    otp = randint(range_start, range_end)
    otp = str(otp)
    return otp