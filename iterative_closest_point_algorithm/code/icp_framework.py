import numpy as np
import math
import matplotlib.pyplot as plt
import time

from misc_tools import *

def closest_point_matching(X, P):
  """
  Performs closest point matching of two point sets.
  
  Arguments:
  X -- reference point set
  P -- point set to be matched with the reference
  
  Output:
  P_matched -- reordered P, so that the elements in P match the elements in X
  """

  P_matched = P

  # TODO: implement

  return P_matched
  
def icp(X, P, do_matching):
  
  P0 = P  
  for i in range(10):  
    # calculate RMSE
    rmse = 0
    for j in range(P.shape[1]):
      rmse += math.pow(P[0,j] - X[0,j], 2) + math.pow(P[1,j] - X[1,j], 2)
    rmse = math.sqrt(rmse / P.shape[1])

    # print and plot
    print("Iteration:", i, " RMSE:", rmse)
    plot_icp(X, P, P0, i, rmse)
    
    # data association
    if do_matching:
      P = closest_point_matching(X, P)
    
    # substract center of mass
    mx = np.transpose([np.mean(X, 1)])
    mp = np.transpose([np.mean(P, 1)])
    X_prime = X - mx
    P_prime = P - mp
    
    # singular value decomposition
    W = np.dot(X_prime, P_prime.T)
    U, s, V = np.linalg.svd(W)
    
    # calculate rotation and translation
    R = np.dot(U, V.T)
    t = mx - np.dot(R, mp)
    
    # apply transformation
    P = np.dot(R, P) + t

  return
    
def main():
  
  X, P1, P2, P3, P4 = generate_data()
  
  icp(X, P1, False)
  #icp(X, P2, False)
  #icp(X, P3, True)
  #icp(X, P4, True)

  plt.waitforbuttonpress()
    
if __name__ == "__main__":
  main()
