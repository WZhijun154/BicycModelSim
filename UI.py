

from input_event import InputEvent
import tkinter as tk

# create a window
window = tk.Tk()
window.title('Bicycle Kinematic Model')
window.geometry('800x600')

# read keyboard input
input_event = InputEvent()
input_event.runThisThread()

# create a changable label
label = tk.Label(window, 
         text='steering_angle = %f, acceleration = %f' % (input_event.steering_angle, input_event.acceleration), 
         font=('Arial', 12), width=30, height=2)

# add the label to the window
label.pack()



# show the window
window.mainloop()
