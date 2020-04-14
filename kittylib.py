# Candy the Catacorn
# By @GalaxyAllieCat
# https://github.com/MermaidAllie/Candy-the-Catacorn

# Cut down into a simple library by Owain Kenway

# Let's go read a few libraries. Catacorns want knowledge!
import board
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogOut, AnalogIn
import touchio
import adafruit_dotstar as dotstar
import time
import random
import pulseio

# Setup everything we use :D
number_stars = 2
eyes = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, number_stars, brightness=0.15)
eye_corners = pulseio.PWMOut(board.EYE_CORNERS, frequency=2000, duty_cycle=0)
paws = pulseio.PWMOut(board.PAWS, frequency=2000, duty_cycle=0)
tail_inner = pulseio.PWMOut(board.TAIL1, frequency=2000, duty_cycle=0)
tail_outer = pulseio.PWMOut(board.TAIL2, frequency=2000, duty_cycle=0)
touch_right_ear = touchio.TouchIn(board.EAR_R)
touch_left_ear = touchio.TouchIn(board.EAR_L)

def left_eye(colour):
	eyes[1] = colour

def right_eye(colour):
	eyes[0] = colour

dark_red = (10,0,0)
red = (255,0,0)

dark_blue = (0,0,10)
blue = (0,0,255)

dark_green = (0,10,0)
green = (0,255,0)

white = (255,255,255)
dark_white = (10,10,10)
black = (0,0,0)
