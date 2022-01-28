kelvin_temp = 301

#convert kelvin to celsius
celsius_temp = kelvin_temp - 273.15

fahrenheit_temp = celsius_temp * (9/5) + 32

import math 

rounded_fahrenheit = math.floor(fahrenheit_temp)

print("The temperature is" , rounded_fahrenheit , "degrees in Fahrenheit")
