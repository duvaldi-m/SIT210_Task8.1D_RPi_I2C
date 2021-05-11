
import time
import board
import adafruit_bh1750
import sys

i2c = board.I2C()
sensor = adafruit_bh1750.BH1750(i2c)

lux_range = [   1,       3,    10,    200,   65535]
value =     ['too dark','dark','meduim','light','too light']
print(f"{value[1]}")

while True:
	try:
		print(f"{sensor.lux:.2f} Lux")
		trigger = True
		lux = sensor.lux
		for idx,x in enumerate(lux_range):
			if lux < x and trigger:	
				print(value[idx])
				trigger = False
		time.sleep(5)

	except KeyboardInterrupt:
		print('exiting....')
		sys.exit()