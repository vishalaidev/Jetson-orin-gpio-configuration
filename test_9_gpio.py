import Jetson.GPIO as GPIO
import time

# 9 GPIO pins (BCM numbering)
pins = [18, 19, 20, 21, 23, 24, 25, 12, 13]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set all pins as output
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

print("Blinking 9 LEDs... Press CTRL+C to stop.")

try:
    while True:
        # Turn all ON
        for pin in pins:
            GPIO.output(pin, GPIO.HIGH)
        time.sleep(0.5)

        # Turn all OFF
        for pin in pins:
            GPIO.output(pin, GPIO.LOW)
        time.sleep(0.5)

except KeyboardInterrupt:
    print("Stopping...")

finally:
    GPIO.cleanup()
