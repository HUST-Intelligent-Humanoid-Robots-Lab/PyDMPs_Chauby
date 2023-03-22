# -*- coding: utf-8 -*-
'''
This code is implemented by Chauby, it is free for everyone.
Email: chaubyZou@163.com
'''

#%% import package
import numpy as np
import matplotlib.pyplot as plt

from dmp_discrete import dmp_discrete

# %%
data_len = 200

demo_traj = np.zeros((2, data_len))
demo_traj[0,:] = np.linspace(0, 1.5*np.pi, data_len)
demo_traj[1,:] = np.sin(demo_traj[0,:])

# %% ----------------- For same initial and goal positions
t = np.linspace(0, 1.0, data_len)

y_demo = np.zeros((2, data_len))
y_demo[0,:] = demo_traj[0,:]
y_demo[1,:] = demo_traj[1,:]


# DMP learning
dmp_1 = dmp_discrete(n_dmps=1, n_bfs=200, dt=1.0/data_len, alpha_y=50, beta_y = 10)
dmp_1.learning(y_demo[0,:], plot=False)

# reproduce learned trajectory
y_reproduce_1_1, dy_reproduce, ddy_reproduce = dmp_1.reproduce()

# set new initial and goal positions
y_reproduce_2_1, dy_reproduce_2, ddy_reproduce_2 = dmp_1.reproduce(tau=1.0, initial=[y_demo[0,0]+1.0], goal=[y_demo[0, -1]-1.0])


dmp_2 = dmp_discrete(n_dmps=1, n_bfs=200, dt=1.0/data_len, alpha_y=50, beta_y = 10)
dmp_2.learning(y_demo[1,:], plot=False)

# reproduce learned trajectory
y_reproduce_1_2, dy_reproduce, ddy_reproduce = dmp_2.reproduce()

# set new initial and goal positions
y_reproduce_2_2, dy_reproduce_2, ddy_reproduce_2 = dmp_2.reproduce(tau=1.0, initial=[y_demo[1,0]], goal=[y_demo[1, -1]-1.0])



plt.figure(figsize=(10, 5))

plt.subplot(2,1,1)
plt.plot(y_demo[0,:], 'g', label='demo x')
plt.plot(y_reproduce_1_1, 'r', label='reproduce x')
plt.plot(y_reproduce_2_1, 'r-.', label='reproduce 2 x')
plt.plot(y_demo[1,:], 'b', label='demo y')
plt.plot(y_reproduce_1_2, 'm', label='reproduce y')
plt.plot(y_reproduce_2_2, 'm-.', label='reproduce 2 y')
plt.legend(loc="upper right")
# plt.ylim(-1.5, 3)
plt.grid()
plt.xlabel('time')
plt.ylabel('y')

plt.subplot(2,1,2)
plt.plot(y_demo[0,:], y_demo[1,:], 'g', label='demo')
plt.plot(y_reproduce_1_1, y_reproduce_1_2, 'r', label='reproduce')
plt.plot(y_reproduce_2_1, y_reproduce_2_2, 'r-.', label='reproduce 2')
plt.legend(loc="upper right")
# plt.ylim(-1.5, 3)
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# %%