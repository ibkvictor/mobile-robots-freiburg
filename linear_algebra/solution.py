import math
import numpy as np
import matplotlib.pyplot as plt

# collecting data
scan = np.loadtxt('laserscan.dat')
angle = np.linspace(-math.pi/2, math.pi/2, scan.shape[0])

# ---(a)
# representing in homogeneous transformation
x_ = scan * np.cos(angle)
y_ = scan * np.sin(angle)


# plot with black markers, label and activate grid
# uncomment plot lines to plot solution1.png
#plt.plot(x_, y_, 'g.')
#plt.ylabel('y')
#plt.xlabel('x')
#plt.grid()


# store image in png
#plt.gca().set_aspect('equal', adjustable='box')
#plt.savefig('solution1.png')

# --- (b)
# scan appears to provide data on other side of wall or structure as though it sees through the wall

# I didnt know a possible explanation, but I checked and it could be that the wall is transparaent or has slits like a fence or gate.

# --- (c)
# computing transformations and points
cat_robot = np.array([1, 0.5, 1]).transpose()
cat_robot_angle = math.pi/4
trans = lambda x_, y_, theta: np.array([[math.cos(theta), -math.sin(theta), x_],[math.sin(theta), math.cos(theta), y_],[0, 0, 1]]))
global_robot_point = np.matmul(trans(0, 0, cat_robot_angle), cat_robot)

x = cat_robot[0]
y = cat_robot[1]
theta = cat_robot_angle
global_robot_trans = trans(x, y, theta)


cat_robot_lazer = np.array([0.2, 0.0, 1]).transpose()
cat_robot_lazer_angle = math.pi
x = 0
y = 0
theta = cat_robot_lazer_angle
robot_lazer_trans = trans(x,y, theta)
robot_lazer_point = np.matmul(robot_lazer_trans, cat_robot_lazer)

global_lazer_point = np.matmul(np.matmul(global_robot_trans, robot_lazer_trans), cat_robot_lazer)
x = cat_robot_lazer[0]
y = cat_robot_lazer[1]
theta = cat_robot_lazer_angle
global_robot_lazer_trans = np.matmul(global_robot_trans, trans(x, y, math.pi))

# perform transformations on laser result
lazer_point = np.stack((x_,y_,np.ones(x_.shape)))
global_lazer_points = np.matmul(global_robot_lazer_trans, lazer_point)

# plot and label
plt.plot(global_lazer_point[0], global_lazer_point[1], 'g.', label= "lazer")
plt.plot(global_robot_point[0], global_robot_point[1], 'r.', label = "robot")
plt.plot(global_lazer_points[0], global_lazer_points[1], "k.", label = "device")
plt.ylabel('y')
plt.xlabel('x')
plt.grid()


# store image in png
plt.gca().set_aspect('equal', adjustable='box')
plt.savefig('solution1_2.png')
