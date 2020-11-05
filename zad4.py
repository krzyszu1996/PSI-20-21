def zmianaC(temp, temperature_type):
    if temperature_type == "F":
        fahrenheit = (temp * 1.8) + 32
        print("{}C = {}F".format(temp, fahrenheit))
    if temperature_type == "R":
        rankine = (temp + 273.15) * 1.8
        print("{}C = {}R".format(temp, rankine))
    if temperature_type == "K":
        kelvin = temp + 273.15
        print("{}C = {}K".format(temp, kelvin))
    if temperature_type != "K" != "F" != "R":
        return "Nieprawidłowy format docelowy temperatury!"


tempC = 19
zmianaC(tempC, "F")
zmianaC(tempC, "R")
zmianaC(tempC, "K")
zmianaC(tempC, "")

