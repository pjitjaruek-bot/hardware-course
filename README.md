# hardware-course

Lesson 1

Pick 3 devices around your home or office, such as an air purifier, a lift, or a rice cooker. For each one, write its sense, think, and act parts in your repo’s README.
Rice cooker: 

Sense: temperature and pressure
Think: has the internal pressure and temperature within the rice cooker reached the desired level
Act: Stop "Cooking" rice but keep rice warm - will change the energy output to lower temperature
Kettle:

Sense: Temperature of the water inside the kettle
Think: HAs the tempareture reached the desired temp
act: Stop adding heat to the water
Refridgerator ligh

Sense: Mechanical button
Think: Is the button pressed or released
Act: If button is released, turn on the light in the fridge. if not, keep dark.

Using EPS32 MicroPython LED Display
Ran this code:

import time

count = 0
while True:
    count = count + 1
    print("Hello", count)
    time.sleep(1)

Import Time = imports "time feature" where time.sleep(X) will tell the code to stop looping for a given amount of seconds. 

Lesson 2

LED have direction. The 3v3 of a ESP32 connects with the A (bent) for ANODE then the C (straight leg) connects with GND. This is because LEDs are a diode which acts as a one-way direction for current movement. Although the current still flows through to complete the circuit, if connected via 3v3 to C to A to GND then the the LED cannot take supply of energy from the current. 

Semiconductors such as LED have their maximum voltage intake. Anything above this will cause damage to the LED. 

Supply Voltage (Current/Resistance) = all voltage spent by LED and resistor - it always adds up to supply voltage
Without an appropriate resistor, the current will become too high and cause LED to burn out. It's the EXCESS CURRENT that is the problem, not the excessive voltage. 

How to calculate the appropriate resistor's resistance
R = (Supply voltage − LED forward voltage) ÷ Current you want 
- there is normally a limit of maximum current so anything that does not exceed this
- The higher the current, the brighter the LED
- In short: the LED sets the voltage split, and the resistor sets the current, preventing the LED from breaking.

Worked example, a red LED on an ESP32 pin at 10 mA:

Leftover voltage: 3.3 − 2.0 = 1.3 V
Resistor: 1.3 ÷ 0.010 = 130 Ω

Round up to a real resistor. Resistors come in standard values: 100, 120, 150, 180, 220, 270, 330, 390, 470, 560, 680, 820, then the same digits ×10 (1 k, 1.2 k, 1.5 k…). Always round up. A slightly bigger resistor means slightly less current, which is safe. Rounding down means more current than you planned. So 130 Ω becomes 150 Ω, which gives about 8.7 mA. The difference in brightness is invisible.

Also check the heat: A resistor turns its slice into heat
Power = Voltage × Current

1.3 V × 10 mA = 13 mW. The small resistors in your kit handle 250 mW (¼ W), so you’re nowhere near the limit. This check matters later with motors.
