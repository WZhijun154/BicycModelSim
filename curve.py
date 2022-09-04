


# a class representing a point which has the x,y and theta properties
class Point:
      def __init__(self, x, y, theta):
         self.x = x
         self.y = y
         self.theta = theta
   
      def __getitem__(self, key):
         # return the state of the vehicle
         if key == 'x':
               return self.x
         elif key == 'y':
               return self.y
         elif key == 'theta':
               return self.theta
   
      def __str__(self):
         return 'x: {}, y: {}, theta: {}'.format(self.x, self.y, self.theta)

      @staticmethod
      def createPoint(position):
         return Point(position[0], position[1], position[2])

import matplotlib.pyplot as plt

# a class representing a curve which has many points
class Curve:
      def __init__(self):
         self.points = []
   
      def addPoint(self, point):
         self.points.append(point)
   
      def __getitem__(self, key):
         return self.points[key]
   
      def __len__(self):
         return len(self.points)

      def kappa(self):
         # compute the curvature of the curve
         kappa = []
         for i in range(len(self.points) - 2):
               p1 = self.points[i]
               p2 = self.points[i + 1]
               p3 = self.points[i + 2]
               kappa.append((p3.y - p2.y) * (p2.x - p1.x) - (p2.y - p1.y) * (p3.x - p2.x))
         return kappa

      def plot(self):
         # plot the curve
         x = [p.x for p in self.points]
         y = [p.y for p in self.points]
         plt.plot(x, y)
         plt.show()