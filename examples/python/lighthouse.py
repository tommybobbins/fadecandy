#!/usr/bin/env python

# Light each LED in sequence, and repeat.

import opc, time

numLEDs = 16
brightness = 256
pulse_time = 0.3
client = opc.Client('localhost:7890')

while True:
	for i in range(numLEDs):
		pixels = [ (0,0,0) ] * numLEDs
		pixels[i] = (brightness,brightness,0)
		client.put_pixels(pixels)
		time.sleep(pulse_time)
