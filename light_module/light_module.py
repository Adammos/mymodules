# light_module.py
# provides API for controlling output of GPIO pins
# uses a script GPIO_output.py, which has to be in the same directory

from subprocess import check_output

# Get path to the GPIO_output.py script
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GPIO_OUTPUT_PATH = os.path.join(BASE_DIR, 'GPIO_output.py')

# Mapping of the lights to their corresponding gpio pins
AVAILABLE_LIGHTS = {1:18, 2:17, 3:21}

ERROR_MESSAGE = "Error in " + os.path.abspath(__file__)
  

# GPIO control API function
def control(light, action):

    # Get gpio pin
    try:
        light = int(light)
        if light in AVAILABLE_LIGHTS.keys():
            pin = AVAILABLE_LIGHTS[light]
        else:
            print ERROR_MESSAGE
            print "control(light, action), light " + str(light) + " not implemented"
            return 0
    except ValueError:
        print ERROR_MESSAGE
        print "control(light, action), light argument not int"
        return 0
    
    # Get gpio pin value
    if action == 'on' or action == True or action == 1:
        value = True
    elif action == 'off' or action == False or action == 0:
        value = False
    else:
        print ERROR_MESSAGE
        print "control(light, action), action argument invalid"
        return 0

    command = 'sudo python ' + GPIO_OUTPUT_PATH + ' ' + str(pin) + ' ' + str(value)
    try:
        output = check_output(command, shell=True)
    except:
        print ERROR_MESSAGE
        print "Error when calling " + GPIO_OUTPUT_PATH + " script"
        return 0

    print output
    return 1

if __name__ == '__main__':
    from time import sleep

    print "Turning on light number 1,2 and 3"
    control(1, True)
    control(2, True)
    control(3, True)
    sleep(1)
    print "Turning off light number 1,2 and 3"
    control(1, False)
    control(2, False)
    control(3, False)
