import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
levels = 2 ** bits
maxVoltage = 3.3
troykaModule = 17
comp = 4


def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


def num2dac(value):
    signal = decimal2binary(value)
    GPIO.output(dac, signal)
    return signal


def findbinary(a, b):
    if (b - a > 1):
        signal = num2dac(int(a + int((b - a) / 2)))
        voltage = (a / levels) * maxVoltage
        time.sleep(0.01)
        compvalue = GPIO.input(comp)
        if (compvalue == 0):
            findbinary(a, a + int((b - a) / 2))
        else:
            findbinary(a + int((b - a) / 2), b)
    else:
        signal = num2dac(int(a + int((b - a) / 2)))
        voltage = (a / levels) * maxVoltage
        print("ADC value = {:^3} -> {}, input voltage = {: .2f}".format(a, signal, voltage))


GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(troykaModule, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
GPIO.setwarnings(False)

try:
    while True:
        findbinary(0, 256)
        time.sleep(0.1)
except KeyboardInterrupt:
    print("The program was stopped by the keyboard")
else:
    print("No exeptions")
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
    print("GPIO cleanup completed")