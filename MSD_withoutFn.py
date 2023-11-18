import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

h = 0.01 # Step size (Increase/decrease to see the change)
t = np.arange(0,20,h)
k = 10 # spring stiffness
m = 1

# Critically damped
c = 1
m_c = np.array([[0, 1],[-k/m, -c/m]])
def ode_func1(t,x):
    return np.dot(m_c,x)
# Under damped
c = 0
m_u = np.array([[0, 1],[-k/m, -c/m]])
def ode_func2(t,x):
    return np.dot(m_u,x)
# Over damped
c =10
m_o = np.array([[0, 1],[-k/m, -c/m]])
def ode_func3(t,x):
    return np.dot(m_o,x)

solve1 = solve_ivp(ode_func1,(0,20),(1,0),t_eval=t)
sc_rk4 = solve1.y

solve2 = solve_ivp(ode_func2,(0,20),(1,0),t_eval=t)
su_rk4 = solve2.y

solve3 = solve_ivp(ode_func3,(0,20),(1,0),t_eval=t)
so_rk4 = solve3.y

plt.figure(figsize=(12,8))
plt.plot(t,su_rk4[0,:])
plt.plot(t,sc_rk4[0,:])
plt.plot(t,so_rk4[0,:])
plt.title("Numerical Solution of MSD System with Varying Dampling")
plt.xlabel("time")
plt.ylabel("displacement")
plt.legend(["no dampling", "c=1", ">critically damped"], loc=1)
plt.grid()
plt.show()
