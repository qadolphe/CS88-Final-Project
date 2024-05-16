import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import odeint
from matplotlib.patches import Circle

# Pendulum rod lengths (m), bob masses (kg).
DIVISIONS = 88362852307
L1, L2 = 1, 1
m1, m2 = 1, 1
# The gravitational acceleration (m.s-2).
g = 9.81

# Maximum time, time point spacings and the time grid (all in s).
tmax, dt = 20, 0.01
t = np.arange(0, tmax+dt, dt)
frames = len(t)

class Pendulum:
    def __init__(self, theta1, dtheta1dt, theta2, dtheta2dt, ax):
        # Do the numerical integration of the equations of motion
        y0 = np.array([theta1, dtheta1dt, theta2, dtheta2dt])
        self.y = odeint(deriv, y0, t, args=(L1, L2, m1, m2))

        # Unpack z and theta as a function of time
        self.theta1 = self.y[:,0]
        self.thetad1 = self.y[:,1]
        self.theta2 = self.y[:,2]
        self.thetad2 = self.y[:,3]

        # Convert to Cartesian coordinates of the two bob positions.
        self.x1 = L1 * np.sin(self.theta1)
        self.y1 = -L1 * np.cos(self.theta1)
        self.x2 = self.x1 + L2 * np.sin(self.theta2)
        self.y2 = self.y1 - L2 * np.cos(self.theta2)

        # Calc binary value
        self.angle_with_axis = np.arctan2(self.x2, self.y2)

        # Initialize empty plot objects
        self.pendulum_lines, = ax.plot([], [], lw=2, c='k')
        self.anchor_point = Circle((0, 0), r/2, fc='k', zorder=10)
        self.bob1 = Circle((0, 0), r, fc='b', ec='b', zorder=10)
        self.bob2 = Circle((0, 0), r, fc='r', ec='r', zorder=10)
    
    def getCart(self):
        return self.x1, self.y1, self.x2, self.y2
    
    def getAngles(self):
        return self.theta1, self.theta2
    
    def getNextInitial(self):
        return self.theta1[frames-1] + np.pi, self.thetad1[frames-1], self.theta2[frames-1] + np.pi, self.thetad2[frames-1]


def deriv(y, t, L1, L2, m1, m2):
    """Return the first derivatives of y = theta1, z1, theta2, z2."""
    theta1, z1, theta2, z2 = y

    c, s = np.cos(theta1-theta2), np.sin(theta1-theta2)

    theta1dot = z1
    z1dot = (m2*g*np.sin(theta2)*c - m2*s*(L1*z1**2*c + L2*z2**2) -
             (m1+m2)*g*np.sin(theta1)) / L1 / (m1 + m2*s**2)
    theta2dot = z2
    z2dot = ((m1+m2)*(L1*z1**2*s - g*np.sin(theta2) + g*np.sin(theta1)*c) + 
             m2*L2*z2**2*s*c) / L2 / (m1 + m2*s**2)
    return theta1dot, z1dot, theta2dot, z2dot

def angleToBinary(angle):
    binSize = np.pi / DIVISIONS
    positive = True
    if angle < 0: positive = False

    binNumber = int(angle / binSize)
    if (binNumber % 2 == 0 and positive) or (binNumber % 2 != 0 and not positive): binary = "0"
    else: binary = "1"

    return binary
    


# Plotted bob circle radius
r = 0.05

# Create figure and axis objects
fig, ax = plt.subplots()
ax.set_xlim((-L1-L2-r), (L1+L2+r))
ax.set_ylim((-L1-L2-r), (L1+L2+r))
ax.set_aspect('equal', adjustable='box')
plt.axis('off')

# Create pendulums
pendulums = []
pendulums.append(Pendulum(3*np.pi/7, 0, 3*np.pi/4, 0, ax))
pendulums.append(Pendulum(3*np.pi/7 + .001, 0, 3*np.pi/4, 0, ax))




# Function to update plot for each frame of the animation
def update(frame):
    # Update positions of pendulum bobs and lines
    for pendulum in pendulums:
        pendulum.bob1.center = (pendulum.x1[frame], pendulum.y1[frame])
        pendulum.bob2.center = (pendulum.x2[frame], pendulum.y2[frame])
        pendulum.pendulum_lines.set_data([0, pendulum.x1[frame], pendulum.x2[frame]], [0, pendulum.y1[frame], pendulum.y2[frame]])


# Add objects to the axis
for pendulum in pendulums:
    ax.add_patch(pendulum.anchor_point)
    ax.add_patch(pendulum.bob1)
    ax.add_patch(pendulum.bob2)

# Create animation
ani = FuncAnimation(fig, update, frames=frames, interval=dt*1000, repeat=False)

nums = []
for i in range(frames):
    binary = ""
    for pendulum in pendulums:
        binary += angleToBinary(pendulum.angle_with_axis[i])
    
    nums.append(int(binary, 2))


ani.save('chaosDemo.mp4', writer='ffmpeg', dpi=800)
