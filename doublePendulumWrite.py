import numpy as np
from scipy.integrate import odeint
import csv

# Pendulum rod lengths (m), bob masses (kg).
DIVISIONS = 88362852307
L1, L2 = 1, 1
m1, m2 = 1, 1
# The gravitational acceleration (m.s-2).
g = 9.81

# Maximum time, time point spacings and the time grid (all in s).
numPend = 8
tmax, dt = 5000, 0.01
t = np.arange(0, tmax+dt, dt)
frames = len(t)

class Pendulum:
    def __init__(self, theta1, dtheta1dt, theta2, dtheta2dt):
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


# Create pendulums
pendulums = []
for i in range(numPend):
    # Initial conditions: theta1, dtheta1/dt, theta2, dtheta2/dt.
    print(f"Pendulum ({i}/{numPend})")
    if i == 0:
        pendulums.append(Pendulum(3*np.pi/7, 0, 3*np.pi/4, 0))
    else:
        t1, dt1, t2, dt2 = pendulums[-1].getNextInitial()
        pendulums.append(Pendulum(t1, dt1, t2, dt2 ))



filename = f"{numPend}P-{tmax}Sec.csv"
nums = []

with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    for i in range(frames):
        binary = ""
        for pendulum in pendulums:
            binary += angleToBinary(pendulum.angle_with_axis[i])
        
        nums.append(int(binary, 2))
        csvwriter.writerow([int(binary, 2)])


