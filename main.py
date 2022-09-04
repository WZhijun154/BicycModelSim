

from bicycle_model import BicycleKinematicModel
from math import pi
from input_event import InputEvent
from time import sleep
from animation import Animation


def main():
      # a test case of the bicycle kinematic model
      # create a bicycle kinematic model
      model = BicycleKinematicModel(
            wheelbase = 2.0,
            max_steering_angle = pi / 6.0,
            max_acceleration = 1.0,
            max_deceleration = -3.0,
            max_speed = 10.0
      )

      # set the initial state of the vehicle
      model.setInitialState(x=0, y=0, theta=0, v=5)

      # print the information of the vehicle
      print(str(model))
      dt = 0.01
      # create a curve object
      # read keyboard input
      input_event = InputEvent()
      input_event.runThisThread()
      # animate the vehicle
      animation = Animation(model)
      animation.runThisThread()
      # simulate the vehicle
      while True:
            # update the state of the vehicle
            model.update(steering_angle=input_event.steering_angle, 
                        acceleration=input_event.acceleration, dt=dt)
            sleep(dt)

# main
if __name__ == '__main__':
      main()