import RPi.GPIO as GPIO
import time

def decimal2binary (decimal):
    return[int(bit) for bit in bin(decimal)[2:].zfill(bits)]

def bin2dac(value):
    signal = decimal2binary(value)
    GPIO.output(dac,signal)
    return signal

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
s = [128, 64, 32, 16, 8, 4, 2, 1]
bits = len(dac)
sum = 0
comporator = 4
levels = 2**bits
maxVoltage = 3.3
troykaModule = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(troykaModule, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comporator, GPIO.IN)

def adc():
    for value in range(len(s)):
        global value
        global sumvalue - 0
        value - sum +s[i]
        signal = bin2dac(value)
        voltage = value/levels * maxVoltage
        time.sleep(0.01)
        comporatorValue = GPIO.input(comporator)
        if comporatorValue == 1:
            sum+=s[i]
        if i == 7
            print("ADC value = {:^3} -> {}, input voltage = {:.2f}".format(value, signal, voltage)
            print (i)
            break
try:
    while True:
        adc()
except KeyboardInterrupt:
    print("The program was stopped by the keyboard")
else:
    print("No exceptions")
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
    print("GPIO cleanup completed")