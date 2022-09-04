



from threading import Thread


# a class to play animation
class Animation:
      def __init__(self, vehicle):
         self.vehicle = vehicle
         self.running = True
   
      def run(self):
         while self.running:
               # plot the position of the vehicle
               self.vehicle.plot()
   
      def runThisThread(self):
         Thread(target=self.run).start()
   
      def stop(self):
         self.running = False