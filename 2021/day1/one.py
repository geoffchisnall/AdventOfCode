#!/usr/bin/env python

import time

file = "input.txt"
line_count = 1
with open(file, 'r') as f:
	previous = next(f).strip()
	for line in f:
		line = line.strip()
		if (line >= previous):
			line_count += 1
#			print(line_count," : INCREASE")
			previous = line
		else:
			previous = line

print("")
print("=====INITIATING SONAR SWEEP=====")
print("")
print('''
                                 |
                               () |
                             /~~~~~~|
                       `~T~T/ U-96  |   c[ ]----     `.
                        `__/___..---t____.[]--------.._`.
        ______..-----~~~~           ___--'--___  <~)    )###-_
   ~~ ~~-~~----..._________..----~~~           ~~~-__--##      ~~--
''')
print("50m")
time.sleep(1)
print("400m")
time.sleep(1)
print("1700m")
time.sleep(1)
print("3000m")
time.sleep(1)
print("12000m")
time.sleep(1)
print("")
print("")
print('''
             ,:',:`,:'
                __||_||_||_||___
           ____[""""""""""""""""]___
          /	                    /
    ~~~~^~^~^^~^~^~^~^~^~^~^~~^~^~^~^~~^~^~
''')
print("         R O C K  B O T T O M   ")
print("")
time.sleep(1)
print("Depth Measurement increased by, %s times." % (line_count))
print("")
time.sleep(1)
print("=====INITIATING SONAR SWEEP SHUTDOWN=====")
print("")
f.close()
