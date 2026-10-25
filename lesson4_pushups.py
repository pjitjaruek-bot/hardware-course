# Readings show the sensors measuring the body's distance from the floor at different timestamps. Like any push up, we start
# at one position from the top and then gradually to go the bottom. Normally if we only state the condition where the code
# counts when the readings is < 10, then it'll count every time the sensor reads < 10 resulting in an overcount. 
# The code must therefore memorize when the user is above a certain threshold, below a certain threshold and back up again
# before triggering a count rep.

# This is done via the if disance AND is_down == False alongside the elif distance AND is_down == True. 
# The code starts at rep 0 and is_down = False
# LINE 17 makes it so that when distance < 10 and is_down == False (preset), we convert the is_down to TRUE
# LINE 17 and 18 does not trigger rep count yet.
# LINE 22 is the trigger to counting. The count is triggered when 2 conditions are met. First is distance must be back up > 30
# and is_down is true. 
# Once these two conditions are met, the output is:
# 1. Reset is_down to False 
# 2. +1 to reps variable 
# 3. Print Rep {}

# Then when all readings are gone through, Print total Reps variable 

readings = [40, 38, 30, 20, 12, 8, 6, 7, 15, 28,
            39, 41, 35, 22, 9, 5, 8, 18, 33, 40]

reps = 0
is_down = False

for distance in readings:
    if distance < 10 and is_down == False:
        is_down = True
    elif distance > 30 and is_down == True:
        is_down = False
        reps += 1
        print(f"Rep {reps}!")

print(f"Total push-ups: {reps}")