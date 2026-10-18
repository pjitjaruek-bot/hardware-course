# hardware-course

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
