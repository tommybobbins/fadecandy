#!/usr/bin/env python

# Open Pixel Control client: All lights to solid white

import opc, time

numLEDs = 256
client = opc.Client('localhost:7890')

black = [ (0,0,0) ] * numLEDs
white = [ (255,255,255) ] * numLEDs
red = [ (255,0,0) ] * numLEDs
blue = [ (0,255,0) ] * numLEDs
green = [ (0,0,255) ] * numLEDs

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
