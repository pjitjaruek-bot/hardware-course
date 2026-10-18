# 1. Ask for supply voltage, LED voltage, and current in mA (as numbers!)

# 2. If the LED voltage is too close to the supply:
#        print a warning
#    otherwise:
#        work out the leftover voltage
#        convert mA to A
#        calculate the resistor
#        calculate the heat in mW
#        print the results
#        if the heat is too high, print a warning

supply_voltage = float(input("Supply Voltage is (V) "))
LED_voltage = float(input("LED Voltage is (V) "))
current_in_mA = float(input("Current is (mA) "))

if LED_voltage > supply_voltage - 0.5:
    print ("Warning, LED voltage is too close to supply voltage")
else:
    leftover_voltage = supply_voltage - LED_voltage
    current_in_A = current_in_mA/1000
    Resistor = leftover_voltage/current_in_A
    Heat = current_in_A * leftover_voltage
    Heat_mW = Heat*1000

    print (f"Heat:{round(Heat_mW)}mW")
    print (f"Resistor Value {round(Resistor)} Ω")

    if Heat_mW > 125:
        print("Warning, heat too high")
    else: 
        print("No warning")



