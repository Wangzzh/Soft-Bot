from voxel import Voxel
import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

class Body:

    def __init__(self, nx, ny, nz):
        self.l = 1
        self.nx, self.ny, self.nz = nx, ny, nz
        self.voxels = [Voxel() for _ in range(nx * ny * nz)]
        for x in range(nx):
            for y in range(ny):
                for z in range(nz):
                    self.voxels[self.i(x,y,z)].D = np.array([x/self.l, y/self.l, z/self.l])
        
        # plotting
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')

    def i(self, x, y, z):
        return x * self.ny * self.nz + y * self.nz + z

    def step(self, t):
        # clear derivative
        for v in self.voxels:
            v.F, v.M = np.zeros(3), np.zeros(3)
        
        # x direction
        for y in range(self.ny):
            for z in range(self.nz):
                for x in range(self.nx - 1):
                    self.__get_derivative__(self.voxels[self.i(x,y,z)], self.voxels[self.i(x+1, y, z)])
        
        # y direction
        for x in range(self.nx):
            for z in range(self.nz):
                for y in range(self.ny - 1):
                    self.__get_derivative__(self.voxels[self.i(x,y,z)], self.voxels[self.i(x, y+1, z)])
        
        # z direction
        for x in range(self.nx):
            for y in range(self.ny):
                for z in range(self.nz - 1):
                    self.__get_derivative__(self.voxels[self.i(x,y,z)], self.voxels[self.i(x, y, z+1)])

        # Euler integration
        for v in self.voxels:
            v.D += t * v.P / v.m 
            v.R += t * v.L / v.I 
            v.P += t * v.F
            v.L += t * v.M

    
    def __get_derivative__(self, A, B):
        # calculate the forces and moments between two voxels
        if A.empty or B.empty:
            return

        # parameters
        Ec = 2 * A.E * B.E / (A.E + B.E)
        Gc = 2 * A.G * B.G / (A.G + B.G)
        a1 = Ec * self.l 
        a2 = Gc * pow(self.l, 3) / 6
        b1 = Ec * self.l 
        b2 = Ec * self.l * self.l / 2
        b3 = Ec * self.l * self.l * self.l / 6

        # forces and momentums
        A.F[0] += a1 * A.D[0] - a1 * B.D[0]
                    

    def plot(self):
        self.ax.scatter([v.D[0] for v in self.voxels], [v.D[1] for v in self.voxels], [v.D[2] for v in self.voxels])
        plt.draw()
        plt.pause(0.01)
        

