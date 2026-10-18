temperature = float(input("Room temperature in °C: "))

if temperature > 30: 
    print ("Fan:High")
elif temperature > 25: 
    print ("Fan:Low")
else:
    print("Fan:OFF")