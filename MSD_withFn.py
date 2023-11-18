import numpy as np
from scipy.integrate import solve_ivp
from functools import partial
import matplotlib.pyplot as plt

def my_msd(t, x, m, c, k):
  
  ds = np.dot(np.array([[0, 1], [-k/m, -c/m]]),x)
  return ds


m = 1
k = 10
f = partial(my_msd, m=m, c=0, k=k)
t_e = np.arange(0, 20, 0.1)
sol_1=solve_ivp(f,(0,20),(1,0),t_eval=t_e)
rk41 = sol_1.y
f = partial(my_msd, m=m, c=1, k=k)
sol_2=solve_ivp(f,(0,20),(1,0),t_eval=t_e)
rk42 = sol_2.y
f = partial(my_msd, m=m, c=10, k=k)
sol_3=solve_ivp(f,(0,20),(1,0),t_eval=t_e)
rk43 = sol_3.y
plt.figure(figsize = (10, 8))
plt.plot(t_e, rk41[0, :])
plt.plot(t_e, rk42[0, :])
plt.plot(t_e, rk43[0, :])
plt.title("Numerical Solution of MSD System with Varying Dampling")
plt.xlabel("time")
plt.ylabel("displacement")
plt.legend(["no dampling", "c=1", ">critically damped"], loc=1)
plt.show()