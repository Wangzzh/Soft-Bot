import numpy as np

class Voxel:

    def __init__(self):
        self.m, self.I = 1, 
        self.D, self.P = np.zeros(3), np.zeros(3) # Linear
        self.R, self.L = np.zeros(3), np.zeros(3) # Angular
        self.dD, self.dP = np.zeros(3), np.zeros(3) # Linear Derivative
        self.dR, self.dL = np.zeros(3), np.zeros(3) # Angular Derivative
        self.E, self.G = 1, 1

    def test(self):
        print("Hello")