import SUNXI_GPIO as GPIO
GPIO.setcfg(231, GPIO.IN) # PH7

while True:
    print(GPIO.input(231))


