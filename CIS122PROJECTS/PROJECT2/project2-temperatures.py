# PROJECT2-TEMPERATURES.PY
import math

F = float(input("Temperature Fahrenheit: "))

C = float(input("Temperature Celsius: "))

def Fahr_to_Celsius(F):
    return C * (9/5)+32
F_output = Fahr_to_Celsius(F)
print("Fahrenheit input to Celsius:" , F_output)

def Celsius_to_Fahr(C):
    return(F - 32)*(5/9)
C_output = Celsius_to_Fahr(C)
print("Celsius input to Fahrenheit:" , C_output)

C = (-40)
F = (-40)

print("When Fahrenheit = Celsius: " , Fahr_to_Celsius(F))
print("When Celsius = Fahrenheit: " , Celsius_to_Fahr(C))
