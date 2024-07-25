import RPi.GPIO as GPIO
import time

def blink_pin(pin, times, interval=1):
    """
    Blink a GPIO pin a specified number of times with a given interval.

    Parameters:
    pin (int): The GPIO pin number.
    times (int): The number of times to blink the pin.
    interval (float): The interval between blinks in seconds (default is 1 second).
    """
    GPIO.setmode(GPIO.BCM)  # or GPIO.BOARD depending on your pin numbering
    GPIO.setup(pin, GPIO.OUT)

    for _ in range(times):
        GPIO.output(pin, True)
        time.sleep(interval)
        GPIO.output(pin, False)
        time.sleep(interval)
    
    GPIO.cleanup()



# Print Board Name
with open('/proc/device-tree/model', 'r') as f:
    model = f.read().strip()
    print(f"This is a {model} board.")


while True:
    # GPIO 17 -> Physical/Board pin 11
    print("GPIO 17 -> Physical/Board pin 11 - START.")
    blink_pin(17,5)
    print("GPIO 17 -> Physical/Board pin 11 - DONE.")

    # GPIO 23 -> Physical/Board pin 16
    print("GPIO 23 -> Physical/Board pin 16 - START.")
    blink_pin(23,5)
    print("GPIO 23 -> Physical/Board pin 16 - DONE.")

    # GPIO 5 -> Physical/Board pin 29
    print("GPIO 5 -> Physical/Board pin 29 - START.")
    blink_pin(5,5)
    print("GPIO 5 -> Physical/Board pin 29 - DONE.")