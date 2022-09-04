


from math import *
import threading
# a class to handle keyboard input events
class InputEvent:
      def __init__(self):
         self.steering_angle = 0.0
         self.acceleration = 0.0
   
      def __getitem__(self, key):
         # return the state of the vehicle
         if key == 'steering_angle':
               return self.steering_angle
         elif key == 'acceleration':
               return self.acceleration
         else:
               raise ValueError('Invalid key')
   
      def __str__(self):
         # return the info of the vehicle
         return 'steering_angle = %f, acceleration = %f' % (self.steering_angle, self.acceleration)

      def readInput(self):
         # read keyboard input
         while True:
               # read keyboard input
               key = input()
               # handle keyboard input
               if key == 'w':
                     self.acceleration = 1.0
               elif key == 's':
                     self.acceleration = -1.0
               elif key == 'a':
                     self.steering_angle = pi / 8.0
               elif key == 'd':
                     self.steering_angle = -pi / 8.0
               elif key == ' ':
                     self.steering_angle = 0.0
                     self.acceleration = 0.0
               elif key == 'q':
                     break
               else:
                     print('Invalid key')

      def runThisThread(self):
         threading.Thread(target=self.readInput).start()
      