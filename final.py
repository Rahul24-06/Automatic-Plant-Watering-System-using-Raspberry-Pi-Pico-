from machine import Pin
import time

red_led = Pin(14, Pin.OUT) #RED LED
green_led = Pin(13, Pin.OUT) #GREEN LED
sensor = Pin(27, Pin.IN, Pin.PULL_DOWN)
pump = Pin(26, Pin.OUT) #pump

import utime
print()
print(" YYYY MM DD HH MM SS")
dateTime = (input ("Enter current date & time: "))+' 0 0'
synchronisedTime = utime.mktime(list(map(int, tuple(dateTime.split(' ')))))
timeDelta = synchronisedTime - int(utime.time())

def timeNow():
    return utime.localtime(utime.time() + timeDelta)

def pump_on():
    red_led.value(1)
    green_led.value(0)
    pump.value(0)
    time.sleep(10)
    print("Pump On - Watering the Plant")
    
def pump_off():
    red_led.value(0)
    green_led.value(1)
    pump.value(1)
    print("Plant is healthy.")
    
while True:
    dateTime = timeNow()
    #print("{:02d}-{:02d}-{:04d} {:02d}:{:02d}:{:02d}".format(dateTime[2],dateTime[1],dateTime[0],dateTime[3],dateTime[4],dateTime[5]))
    utime.sleep(1)
    if (dateTime[3] == 8 and dateTime[3] == 16 and dateTime[3] == 0):
        if (dateTime[4] == 0 and dateTime[5] == 0):
            pump_on()
        else:
            pump_off()
            
    elif sensor.value():
        pump_on()
        
    else:
        pump_off()
        
        



