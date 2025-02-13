#import libraries
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import utime as time
from dht import DHT11, InvalidChecksum
import sys

#define oled i2c pins and initialise
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

#define leds
led = machine.Pin(25, machine.Pin.OUT)
led.value(1)
led1 = machine.Pin(2, machine.Pin.OUT)
led2 = machine.Pin(3, machine.Pin.OUT)
led3 = machine.Pin(4, machine.Pin.OUT)
led4 = machine.Pin(5, machine.Pin.OUT)

#welcome message
led1.value(0)
led2.value(0)
led3.value(0)
led4.value(0)
oled.fill(0)
oled.text("Hello mum",0,0)
oled.show()
led1.value(1)
time.sleep(3)
led1.value(0)
led2.value(1)
oled.fill(0)
oled.text("Checking", 0,0)
oled.text("the room", 0,10)
oled.show()
time.sleep(3)
led2.value(0)
led3.value(1)
oled.fill(0)
oled.text("Hope you're", 0,0)
oled.text("well", 0, 10)
oled.show()
time.sleep(2)
led3.value(0)
led4.value(1)
oled.fill(0)
oled.text("Don't forget", 0, 0)
oled.text("to tidy your", 0, 10)
oled.text("Do Do room", 0, 20)
oled.show()
time.sleep(2)
led1.value(1)
led2.value(2)
led3.value(3)
oled.fill(0)
oled.text("Remember...", 0,0)
oled.text("You're",0,10)
oled.text("very special",0,20)
oled.show()
time.sleep(2)
led1.value(0)
led2.value(0)
led3.value(0)
led4.value(0)
time.sleep(0.5)
led1.value(1)
led2.value(1)
led3.value(1)
led4.value(1)
time.sleep(0.5)
led1.value(0)
led2.value(0)
led3.value(0)
led4.value(0)
time.sleep(0.5)

#DHT11
pin = Pin(28, Pin.OUT, Pin.PULL_DOWN)
sensor = DHT11(pin)

# loop
while True:
    led.value(1)
    led1.value(1)
    led2.value(1)
    led3.value(1)
    led4.value(1)
    time.sleep(2)
    led.value(0)
    
    # Clear the oled display in case it has junk on it.
    oled.fill(0)       
    
    # Add some text
    oled.text("Mums",0,0)
    oled.text("Do Do Room", 0, 10)
    oled.text("Temp: ",10,30)
    oled.text(str(sensor.temperature),50,30)
    oled.text("*C",90,30)
    
    oled.text("Humi: ",10,50)
    oled.text(str(sensor.humidity),50,50)
    oled.text("%",90,50)
    oled.show()
