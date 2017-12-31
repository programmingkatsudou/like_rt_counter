import RPi.GPIO as GPIO
import time
import twitter
import os
import sys

def encode(num):
    if num == 0:
        return format(0x7E, 'b')
    elif num == 1:
        return '0' + format(0x30, 'b')
    elif num == 2:
        return format(0x6D, 'b')
    elif num == 3:
        return format(0x79, 'b')
    elif num == 4:
        return '0' + format(0x33, 'b')
    elif num == 5:
        return format(0x5B, 'b')
    elif num == 6:
        return format(0x5F, 'b')
    elif num == 7:
        return format(0x70, 'b')
    elif num == 8:
        return format(0x7F, 'b')
    elif num == 9:
        return format(0x7B, 'b')
    else:
        return "err"

def display(pins, flags):
    for pin, flag in zip(pins, flags):
        if flag == "1":
            GPIO.output(pin, GPIO.HIGH)
        elif flag == "0":
            GPIO.output(pin, GPIO.LOW)

def gpio_init(pins, digs):
    GPIO.setmode(GPIO.BOARD)
    for pin in pins+digs:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

if __name__ == "__main__":
    #A:11, B:7, C:4, D:2, E:1, F:10, G:5
    #EDCGBFA
    pins = [19, 13, 7, 5, 3, 15, 11]
    #pins = [3, 5, 7, 11, 13, 15, 19]
    digs  = [31, 33, 35, 37]
    gpio_init(pins, digs)    
    try:
        for i in range(0, 10):
            display_setter(pins, encoder(i))
            time.sleep(1)
        for pin in pins:
            GPIO.output(pin, GPIO.LOW)
    except KeyboardInterrupt:
        print("cleanup...\n")
    finally:
        GPIO.cleanup()
