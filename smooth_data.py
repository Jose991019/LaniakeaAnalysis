import h5py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
archivos = [1,3,7,10]
filename = 'velocity_AbacusCosmos_720box_planck_00_0_FoF_vmax_300.0_sigma_{}.0_nside_360.hdf5'

velocidades = []
velocidades2 = []

divergencias = []
datos_seleccionados = []
datos_seleccionados2 = []

aleatorio = np.random.randint(0,360)
for i in archivos:
    with h5py.File(filename.format(i), 'r') as f:
        print(f.keys())
        divergence = list(f.keys())[0]
        vel_x = list(f.keys())[1]
        vel_y = list(f.keys())[2]
        vel_z = list(f.keys())[3]

        dataDivergence = list(f[divergence])
        data_vel_x = np.array(f[vel_x])
        data_vel_y = np.array(f[vel_y])
        data_vel_z = np.array(f[vel_z])
    velocidades.append(np.sqrt(data_vel_x**2 + data_vel_y**2 + data_vel_z**2))
    divergencias.append(dataDivergence)
    datos_seleccionados.append(np.array(dataDivergence[aleatorio])[:120,:120])
    if (i == 3):
        datos_seleccionados2 = np.array(dataDivergence[aleatorio])[:100, :100]
        velocidades2 = [data_vel_x[aleatorio][:100,:100] , data_vel_y[aleatorio][:100,:100], data_vel_z[aleatorio][:100,:100]]



plt.figure(figsize = (10,10))
for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(datos_seleccionados[i])
    plt.colorbar()
    plt.title(r"$\sigma_{{Vox}} $ = {}vx".format(archivos[i]))

plt.savefig("Suavizados.png")

rangos = [(0,40),(0,25),None,None]
plt.figure(figsize = (10,10))
for i in range(4):
    vel_actual = []
    plt.subplot(2,2,i+1)
    plt.hist(velocidades[i].flatten(), bins = 50, density = True,edgecolor = 'black', range = rangos[i])
    plt.title(r"$\sigma_{{Vox}} $ = {}vx".format(archivos[i]))
    plt.xlabel("Speed[km/s]")
    plt.ylabel("$N_{voxels}/Total_{voxels}$")

plt.savefig("smooth_dist.png")

plt.figure(figsize = (10,10))
plt.imshow(datos_seleccionados2)
plt.colorbar()
plt.quiver(velocidades2[2],velocidades2[0])

plt.savefig("Suavizados2.png")