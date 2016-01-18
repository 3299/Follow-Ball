import wpilib
from wpilib import RobotDrive
import ball_functions as bf

class MyRobot(wpilib.SampleRobot):

    def robotInit(self): #Inits the robot
        #Setup drive object
        self.robotDrive = wpilib.RobotDrive(0, 2, 1, 3) #frontLeftMotor, rearLeftMotor, frontRightMotor, rearRightMotor
        self.robotDrive.setExpiration(0.1)

        #Invert motors
        self.robotDrive.setInvertedMotor(RobotDrive.MotorType.kFrontLeft, True)
        self.robotDrive.setInvertedMotor(RobotDrive.MotorType.kRearLeft, True)
        self.robotDrive.setInvertedMotor(RobotDrive.MotorType.kFrontRight, True)
        self.robotDrive.setInvertedMotor(RobotDrive.MotorType.kRearRight, True)

        #Joysticks 1 & 2 on the driver station
        self.leftStick = wpilib.Joystick(0)
        self.rightStick = wpilib.Joystick(1)

    def operatorControl(self):
        self.robotDrive.setSafetyEnabled(True)

        while self.isOperatorControl() and self.isEnabled():

            #Left joystick trigger makes robot follow ball
            if (self.leftStick.getTrigger):
                angle = bf.calculateBallAngle() #Get angle to ball

                curve = bf.remap(angle, 0, 360, -1, 1) #Scale angle to value accepted by drive()
                self.robotDrive.drive(0.5, curve)

            self.robotDrive.tankDrive(self.leftStick, self.rightStick) #Drive with joysticks
            wpilib.Timer.delay(0.005) # wait for a motor update time

if __name__ == '__main__':
    wpilib.run(MyRobot)
