#   --------------Importing neseccary libraries ------------

import machine
import time
import dht

#  ------- Setting up DH11 sensor ---------

dht_pin = machine.Pin(15)
dht_sensor = dht.DHT11(dht_pin)

#  ----------- Setting up Raindrop sensor to pin 26-------

raindrop_sensor = machine.ADC(26)

# ------- Setiing up LDR to pin 27-------

ldr_sensor = machine.ADC(27)

# ------- Setting up Bluetooth with buad rate of 9600  -----

uart = machine.UART(0, baudrate = 9600)

# ------ Creating a function for data retrieval ---------

def read_dht():                              
    dht_sensor.measure()               # ------- Triggers the DHT11 sensor to take measurments ------
    temp = dht_sensor.temperature()
    humidity = dht_sensor.humidity()
    return temp. humidity

def read_raindrop():
    return raindrop_sensor.read_u16()     # ---- Return a 16-bit value ranging from 0 to 65535 -----

def read_idr():
    return idr_sensor.read_u16()          # ---- Return a 16-bit value -----

def send_via_bluetooth(data):
    uart.write(data + '\n')
    
while True:
    temp, humidity = read_dht()
    rain = read_raindrop()
    light = read_idr()
    
    data = f'Temp: {temp}C, Humidity: {humidity}%, Rain: {rain}, Light: {light}'
    print(data)
    send_via_bluetooth(data)
    
    time.sleep(2)  # ------- Adjust the delay needed ---------
    
    
    
    
    

