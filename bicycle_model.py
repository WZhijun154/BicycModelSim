


from math import *
from curve import *

# a class representing a bicycle kinematic model of a vehicle
class BicycleKinematicModel:
      def __init__(self, wheelbase, max_steering_angle,  max_acceleration, max_deceleration , max_speed):
         self.wheelbase = wheelbase
         self.max_steering_angle = max_steering_angle
         self.max_acceleration = max_acceleration
         self.max_deceleration = max_deceleration
         self.max_speed = max_speed
         self.width = wheelbase / 2.0

         # state of the vehicle
         self.x = 0
         self.y = 0
         self.theta = 0
         self.v = 0
         
      def setInitialState(self, x, y, theta, v):
         # set the initial state of the vehicle
         self.x = x
         self.y = y
         self.theta = theta
         self.v = v

      def update(self, steering_angle, acceleration , dt):
         # update the state of the vehiclee
         # steering_angle: steering angle of the vehicle
         # acceleration: acceleration of the vehicle
         # dt: time step
   
         # check if the steering angle is within the limit
         if abs(steering_angle) > self.max_steering_angle:
               raise ValueError('Steering angle is out of range')
   
         # check if the acceleration is within the limit
         if acceleration > self.max_acceleration:
               raise ValueError('acceleration is out of range')
   
         # check if the deceleration is within the limit
         if acceleration < self.max_deceleration:
               raise ValueError('deceleration is out of range')

         # compute the new state of the vehicle
         self.x = self.x + self.v * dt * cos(self.theta)
         self.y = self.y + self.v * dt * sin(self.theta)
         self.theta = self.theta + self.v * dt * tan(steering_angle) / self.wheelbase
         self.v = self.v + dt * acceleration

         # check if the velocity is within the limit
         if self.v > self.max_speed:
            self.v = self.max_speed
         elif self.v < 0:
            self.v = 0
   
      def __getitem__(self, key):
         # return the state of the vehicle
         if key == 'x':
               return self.x
         elif key == 'y':
               return self.y
         elif key == 'theta':
               return self.theta
         elif key == 'v':
               return self.v
         elif key == 'position':
               return self.x,self.y,self.theta
         else:
               raise ValueError('Invalid key')

      def print_state(self):
         # print the state of the vehicle
         print('x = %f, y = %f, theta = %f, v = %f' % (self.x, self.y, self.theta, self.v))


      def plot(self):
            # plot the position of the vehicle
            from matplotlib import pyplot as plt
            plt.plot(self.x, self.y, 'ro')
            plt.plot([self.x, self.x + self.width * cos(self.theta)], [self.y, self.y + self.width * sin(self.theta)], 'r-')
            plt.plot([self.x, self.x - self.width * cos(self.theta)], [self.y, self.y - self.width * sin(self.theta)], 'r-')
            plt.axis('equal')
            plt.grid(True)
            plt.pause(0.01)


      def __str__(self):
         # return the info of the vehicle
         return 'wheelbase = %f, max_steering_angle = %f, max_acceleration = %f, max_deceleration = %f, max_speed = %f'  % (self.wheelbase, self.max_steering_angle, self.max_acceleration, self.max_deceleration, self.max_speed)



