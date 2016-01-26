import math
#import pprint
import networktables
from networktables import NetworkTable
ball = NetworkTable.getTable('/GRIP/ball')

cameraW = 240
cameraL = 320

def calculateBallAngle():
    ballX = networktables.NumberArray()
    ballY = networktables.NumberArray()
    ball.retrieveValue("x", ballX)
    ball.retrieveValue("y", ballY)

    if (len(ballX) == 1):
      ballX = float(ballX[0])
      ballY = float(ballY[0])

      robotX = cameraL / 2 # Robot is assumed to virtually be in the middle of camera grid

      '''We create a right triangle between bottom of camera grid, the ball, and the robot'''
      d = robotX - ballX # Length of bottom leg
      adj = abs(d)
      hyp = math.sqrt(ballY**2 + adj**2)
      angle = math.degrees(math.acos((adj/hyp))) # Angle between robot and ball (acos() returns radians, so we convert to degrees)

      if (d < 0): # If bottom leg is negative ball is to the right
        angle = angle + 90

      print(angle)

      return angle

    else: # If no value is found don't move
      return 0

def remap(x, oMin, oMax, nMin, nMax):
    #range check
    if oMin == oMax:
        print("Warning: Zero input range")
        return None

    if nMin == nMax:
        print("Warning: Zero output range")
        return None

    #check reversed input range
    reverseInput = False
    oldMin = min( oMin, oMax )
    oldMax = max( oMin, oMax )
    if not oldMin == oMin:
        reverseInput = True

    #check reversed output range
    reverseOutput = False
    newMin = min( nMin, nMax )
    newMax = max( nMin, nMax )
    if not newMin == nMin :
        reverseOutput = True

    portion = (x-oldMin)*(newMax-newMin)/(oldMax-oldMin)
    if reverseInput:
        portion = (oldMax-x)*(newMax-newMin)/(oldMax-oldMin)

    result = portion + newMin
    if reverseOutput:
        result = newMax - portion

    return result
