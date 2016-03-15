# GPIO_output.py %gpio %value
# The script when called sets a GPIO to high or low
# Must be run as root

import os
from sys import argv

try:
    import RPIO
except:
    print "import error in " + os.path.abspath(__file__)
    print "Could not import RPIO, try running as root."    
    exit()

def print_usage():
    print "The script when called sets a GPIO to high or low"
    print "usage: sudo python " + __file__ + " gpio value"
    print "gpio: one of the GPIO pins (int). GPIO layout is revision 1."
    print "action: True, False, 0, 1"

if len(argv) > 1:
    if argv[1] == '--help':
        print_usage()
        exit()

if len(argv) != 3:
    print "Error: Wrong number of arguments"
    print "run --help"
    exit()

# All available GPIO pins
gpio_list = [0,1,4,7,8,9,10,11,14,15,17,18,21,22,23,24,25]

# Get first argument - gpio pin
try:
    pin = int(argv[1])
    if pin not in gpio_list:
        print "Error: gpio argument not in a range of gpio pin numbers"
        print "Valid GPIO: " + str(gpio_list)
        exit()
except ValueError:
        print "Eror: gpio argument not a number"
        print "run --help"
        exit()

# Get second argument - value
value = argv[2]
if value == 'True' or value == 'true' or value == '1':
    value = True
elif value == 'False' or value == 'false' or value == '0':
    value = False
else:
    print "Error: gpio value invalid"
    print "run --help"
    exit()

# Set GPIO
RPIO.setwarnings(False)
try:
    RPIO.setup(pin, RPIO.OUT)
    RPIO.output(pin, value)
    print "OK"
except:
    print "Error when setting GPIO in " + os.path.abspath(__file__)
    exit()

