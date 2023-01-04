# Taofik Ahmed Suleiman, and Daniel Tweneboah Anyimadu

# This is a special program to define some parameters about the pedestrian in other to reduce the complesity of the code.
# This file will be imported to the main program file

signals = []
noOfSignals = 4


speeds = 0.15   # average speeds of vehicles

# Coordinates of pedestrians start
x = {'right':0, 'down':697, 'left':1400, 'up':657}
y = {'right':398, 'down':0, 'left':436, 'up':800}

vehicles = {'right':[], 'crossed':0, 'down':[],'crossed':0,'left':[],'crossed':0, 'up': [], 'crossed':0}

directionNumbers = {0:'right', 1:'down', 2:'left', 3:'up'}

# Coordinates of signal image, timer, and vehicle count
signalCoods = [(530,209),(817,200),(827,570),(522,570)]

# Coordinates of Horizontal signal image, timer, and vehicle count
signalCoodsHorizontal = [(500,300),(785,300),(795,537),(500,537)]

# Coordinates of stop lines
stopLines = {'right': 590, 'down': 330, 'left': 800, 'up': 535}
defaultStop = {'right': 580, 'down': 320, 'left': 810, 'up': 545}

# Gap between vehicles
stoppingGap = 40    # stopping gap
movingGap = 40   # moving gap



class TrafficSignal:
    def __init__(self, red, green):
        self.red = red
        self.green = green