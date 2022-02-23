# author: Victor Ezekiel, github.com/ibkvictor
import math
import numpy as np

# --- (a)
def diffdrive(x, y, theta, v_l, v_r, t, l):
	# circular motion
	if(v_r == v_l):
		x_n = x + 1/2 * (v_l + v_r) * math.cos(theta)

		y_n = y + 1/2 * (v_l + v_r) * math.sin(theta)
		return [x_n, y_n, theta]
	#circular motion
	else:
		rot = lambda w, t : np.array([[math.cos(w * t), -math.sin(w * t), 0], [math.sin(w * t), math.cos(w * t), 0], [0, 0, 1]])
		position = np.array([x, y, theta]).T

		R = 0.5 * (l * (v_l + v_r)/(v_r - v_l))
		w = (v_r - v_l)/l
		v = (v_r + v_l)/2
		ICC = [(x - R * math.sin(theta)), (y + R * math.cos(theta))]
	
		return (list(np.matmul(rot(w, t), position - np.array(ICC + [0]).T) + np.array(ICC + [w * t]).T))


# --- (b)

def control():
	x = 1.5
	y = 2.0
	theta = math.pi/2
	l = 0.5
	data = [[0.3, 0.3, 3], [0.1, -0.1, 1], [0.2, 0, 2]]
	for v_l, v_r, t in data:
		x, y, theta = diffdrive(x, y, theta, v_l, v_r, t, l)

	print("x: ", x)
	print("y: ", y)
	print("theta: ", theta)

control()
