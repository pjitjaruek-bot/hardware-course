# while True is paired with again where it allows us to prompt the code to ask for new sets of input to rerun the code
# Commonly while True is the overarching function for the entire code, hence one indent after while True: for the whole code then closed
# with again, if condition to break.

standard = [100, 120, 150, 180, 220, 270, 330, 390, 470, 560, 680, 820, 1000,
            1200, 1500, 1800, 2200, 2700, 3300, 3900, 4700, 5600, 6800, 8200]


while True: 

    supply_voltage = float(input("Supply voltage (V): "))
    led_voltage = float(input("LED voltage (V): "))
    current_mA = float(input("Current (mA): "))

    if led_voltage > supply_voltage - 0.5:
        print("Warning: LED voltage is too close to supply voltage")
    else:
        leftover_voltage = supply_voltage - led_voltage
        exact_resistor = leftover_voltage / (current_mA / 1000)
        print(f"Exact resistor: {round(exact_resistor)} Ω")

        if exact_resistor > 8200:
            print("Too high: no standard resistor in the list is big enough")
        else:
            for r in standard:
                if exact_resistor <= r:
                    chosen = r
                    break

            actual_current_mA = leftover_voltage / chosen * 1000
            actual_heat_mW = leftover_voltage * actual_current_mA

            print(f"Resistor to buy: {chosen} Ω")
            print(f"Actual current: {round(actual_current_mA, 1)} mA")
            print(f"Actual heat: {round(actual_heat_mW, 1)} mW")

            if actual_heat_mW > 125:
                print("Warning: heat too high, use a bigger resistor")
            else:
                print("No warning")
            
    again = input("Another? (y/n) ")
    if again == "n":
        break
        
