import numpy as np

class Voxel:

    def __init__(self):
        self.empty = False
        self.m, self.I = 1, 1
        self.D, self.P = np.zeros(3), np.zeros(3) # Linear
        self.R, self.L = np.zeros(3), np.zeros(3) # Angular
        self.F, self.M = np.zeros(3), np.zeros(3) # Force & Moment
        self.E, self.G = 1e8, 1e-3
        
        # Young's Modulus E
        # Rubber: 1e8 Pa, Steel: 2e11 Pa
        # Shear Modulus G
        # Rubber 6e-4 Pa, Steel: 80 Pa
        