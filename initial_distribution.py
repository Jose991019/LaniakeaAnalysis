import AbacusCosmos.Halos as ach
from astropy.table import Table
import matplotlib.pyplot as plt
import numpy as np
import glob
import os
from collections import Counter
import scipy.ndimage as scpimg
import h5py


path = "C:/AbacusCosmos/"
halo_data = ach.read_halos_FoF(path)
velocidades = halo_data['vel']
posiciones = halo_data['pos']
pos_x = posiciones[:,0]
pos_y = posiciones[:,1]
pos_z = posiciones[:,2]

vel_x = velocidades[:,0]
vel_y = velocidades[:,1]
vel_z = velocidades[:,2]

VDC = np.gradient(vel_x) + np.gradient(vel_y) + np.gradient(vel_z)
abs_speed = np.sqrt(vel_x**2+vel_y**2+vel_z**2)

plt.figure(figsize = (7,10))
plt.subplot(2,1,2)
plt.hist(VDC.flatten(), bins = 50, density = True,edgecolor = 'black', range = (-2000,2000))
plt.title("Initial VDC distribution")
plt.xlabel("VDC[km/s]")
plt.ylabel("$N_{voxels}/Total_{voxels}$")
plt.subplot(2,1,1)
plt.hist(abs_speed.flatten(), bins = 50, density = True,edgecolor = 'black', range = (0,2000))
plt.title("Initial absolute speed distribution")
plt.xlabel("Speed[km/s]")
plt.ylabel("$N_{voxels}/Total_{voxels}$")
plt.savefig('initial_distribution.png')
