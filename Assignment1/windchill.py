#INPUT temperature in Fahrenheit T, wind speed in mph V
#RETURN wind chill temperature
def windChill(T,V):
    t_zero = 35.74
    return t_zero + 0.6215 * T - 35.75 * V**.16 + .4275*T * V**.16
     
print(windChill(25,5))