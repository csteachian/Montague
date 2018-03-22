
#!/usr/bin/python3
import scrollphathd as sphd
import time, sys, tty, termios, os
from urllib import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://feeds.bbci.co.uk/news/rss.xml").read()
soup = BeautifulSoup(html, "html.parser")

headlines = ""
for tag in soup.find_all("title"):
  temp = str(tag)
  headlines += temp[16:-11]+" | "



values =     [5,4,3,2,1,2,3,4,5,6,7,8,9,8,7,6,5]
multiplier = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

# with thanks to Jon Witts (www.jonwitts.co.uk/archives/896)
def getch():
  fd = sys.stdin.fileno()
  old_settings = termios.tcgetattr(fd)
  try:
    tty.setraw(sys.stdin.fileno())
    ch = sys.stdin.read(1)

  finally:
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
  return ch

def changeValue(index):
  global values
  global multiplier
  num = values[index]
  mult = multiplier[index]
  if (num > 9) or (num < 1):
    mult = mult * -1
  num = num + mult
  values[index] = num
  multiplier[index] = mult

def graphAnim():
  sphd.set_brightness(0.2)
  sphd.set_graph(values,3,7,1.0,0,0,17,6)
  sphd.show()
  for index in range(0,17):
    changeValue(index)
    time.sleep(0.008)

def drawHeart():
  buffer1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,
             0,0,0,0,0,1,1,1,0,1,1,1,0,0,0,0,0,
             0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,
             0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,
             0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]

  buffer2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,
             0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,
             0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

  animbuffer = [buffer1, buffer2]
  frames = 2

  for loop in range(0,10):
    pic = animbuffer[loop % frames]
    for pos in range(0,len(pic)):
      xpos = pos % 17
      ypos = int(pos / 17)
      sphd.set_pixel(xpos,ypos,float(pic[pos]))
    sphd.show()
    time.sleep(1)

def showFact(message):
  message = message[:255] # cut down to 255 chars
  message += "....."
  print("Fact: ",message)
  sphd.write_string(message)
  for x in range(0,((len(message)-4)*5)):
    sphd.show()
    sphd.scroll(1)
    time.sleep(0.01)
  time.sleep(0.4)
  sphd.clear()
  sphd.show()

button_delay = 0.2
sphd.set_brightness(0.3)
#sphd.rotate(180)
print('a,b,c or x')
while True:
  sphd.clear()
  char = getch()
  if (char == "a"):
    drawHeart()
    time.sleep(button_delay)
  elif (char == "b"):
    for x in range(0,50):
      graphAnim()
    time.sleep(button_delay)
  elif (char == "c"):
    showFact("Montague is ready...")
    time.sleep(button_delay)
  elif (char == "t"):
    showFact("THNX PITOP")
    time.sleep(button_delay)
  elif (char == "n"):
    showFact(headlines)
    time.sleep(button_delay)
  elif (char == "x"):
    exit(0)

