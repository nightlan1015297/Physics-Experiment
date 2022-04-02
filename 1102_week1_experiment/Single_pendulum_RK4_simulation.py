 
import matplotlib.pyplot as plt 
import numpy as np

G = 9.8
R = 1
gamma = 0

initial_theta = 10
initial_velocity = 0


def dv (t,theta,v):
    return -G/R*np.sin(theta/360*2*np.pi)-gamma*v
def dtheta(t,theta,v):
    return v

t_start = 0
t_end   = 50
dt = 0.0001

iter_times = int((t_end-t_start)/dt)

time_sequence = [0]
velocity_sequence = [initial_velocity]
theta_sequence = [initial_theta]

for i in range(iter_times):
    k_vel1 = dv(time_sequence[i],theta_sequence[i],velocity_sequence[i])
    k_theta1 = dtheta(time_sequence[i],theta_sequence[i],velocity_sequence[i])
    k_vel2 = dv(time_sequence[i]+dt/2,theta_sequence[i]+dt/2*k_theta1,velocity_sequence[i]+dt/2*k_vel1)
    k_theta2 = dtheta(time_sequence[i]+dt/2,theta_sequence[i]+dt/2*k_theta1,velocity_sequence[i]+dt/2*k_vel1)
    k_vel3 = dv(time_sequence[i]+dt/2,theta_sequence[i]+dt/2*k_theta2,velocity_sequence[i]+dt/2*k_vel2)
    k_theta3 = dtheta(time_sequence[i]+dt/2,theta_sequence[i]+dt/2*k_theta2,velocity_sequence[i]+dt/2*k_vel2)
    k_vel4 = dv(time_sequence[i]+dt,theta_sequence[i]+dt*k_theta3,velocity_sequence[i]+dt*k_vel3)
    k_theta4 = dtheta(time_sequence[i]+dt,theta_sequence[i]+dt*k_theta3,velocity_sequence[i]+dt*k_vel3)
    velocity_sequence.append(velocity_sequence[i] + dt/6*(k_vel1+2*k_vel2+2*k_vel3+k_vel4))
    theta_sequence.append(theta_sequence[i] + dt/6*(k_theta1+2*k_theta2+2*k_theta3+k_theta4))
    time_sequence.append(time_sequence[i]+dt)

plt.plot(time_sequence,theta_sequence)
plt.xlabel('time')
plt.ylabel('theta')
plt.show()

