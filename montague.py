#!/usr/bin/python

import scrollphathd as sphd
import time

sphd.set_brightness(0.3)
sphd.rotate(180)
sphd.write_string("Montague is ready...")
while True:
  sphd.show()
  sphd.scroll(1)
  time.sleep(0.1)
