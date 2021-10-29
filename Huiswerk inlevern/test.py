""" Animation of a sine wave with matplotlib 
    Rufus Fraanje, 05/10/2020
    For more information on sinusoid waves, see
    https://nl.wikipedia.org/wiki/Golf_(natuurkunde)
    
    Als je spyder gebruikt, zorg dat de ipython graphics backend op automatic staat!
    Tools -> Preferences -> IPython console -> Graphics tab -> Backend: Automatic.
    Daarna herstarten van ipython console met bijv. Ctrl + ., of opnieuw opstarten van spyder.
"""

import numpy as np
import matplotlib.pyplot as plt

f          = 1          # Hz, frequency
omega      = 2*np.pi*f  # rad/s, angular frequency 
wavelength = 0.5        # m
wavenumber = 2*np.pi/wavelength # m^(-1)

x = np.linspace(0,3*wavelength,100) # points in space

# When you are not using spyder, and see that plt.show() is blocking
# you have to command matplotlib to be non-blocking, you can do this by uncommenting next line:
# plt.ion()
# which turns on the interactive mode, you can turn it off with plt.ioff().
fig, ax = plt.subplots() # create a figure with an axis object
plt.show()               # directly show the figure

for t in np.linspace(0,3,100): # for number of times
    y = np.sin(wavenumber*x - omega*t) # calculate the wave
    ax.plot(x,y)         # plot the wave y as function of place x
    plt.xlim(x[0],x[-1]) # set limits on horizontal axis
    plt.ylim(-1,1)       # set limits on vertical axis
    fig.canvas.draw()    # redraw window, you may use plt.draw() as well
    plt.pause(0.1)       # use this to wait a short time before updating the graph
                         # sleep from the time module does not work for me
    ax.cla()             # clear axis else new plot will be drawn on top of previous

plt.close(fig)           # close figure







