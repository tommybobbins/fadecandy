#!/usr/bin/env python

# Open Pixel Control client: All lights to solid white

import opc, time

numLEDs = 16
brightness = 64
client = opc.Client('localhost:7890')

black = [ (0,0,0) ] * numLEDs
white = [ (brightness,brightness,brightness) ] * numLEDs
red = [ (brightness,0,0) ] * numLEDs
blue = [ (0,brightness,0) ] * numLEDs
green = [ (0,0,brightness) ] * numLEDs

while True:
    client.put_pixels(white)
    time.sleep(0.05) 
    client.put_pixels(red)
    time.sleep(0.05) 
    client.put_pixels(blue)
    time.sleep(0.05) 
    client.put_pixels(green)
    time.sleep(0.05) 
    client.put_pixels(black)
    time.sleep(0.05)
