#  ***********************************************************************************************
#  *           THIS IS THE SIMULATION FOR SERIES RLC CIRCUIT USING RUNGE-KUTTA METHOD            *
#  *         YOU CAN USE ANY CONFIGURATION OF R, L, C TO SEE WHAT WILL HAPPENS IN RESULT         *
#  *  REMEMBER "DO NOT" USE THE CONFIGURATION OF R, L, C PAREMETERS WITH LARGE SCALE DIFFERENCE  *
#  * THIS MAY BREAK THE STABILITY OF RK4 METHOD SINCE THE TIME INTERVAL IN THIS PROGRAM IS FIXED *
#  ***********************************************************************************************


    
import matplotlib.pyplot as plt 



R = 2
C = 12
L = 5

initial_voltage = 0
initial_current = 0

Vsource_max = 10
def dI (t,i,v):
    return C*Vin(t)-C*v-R*i/L 

def dV(t,i,v):
    return i/C

def Vin(t):
    if t>25:
        return 0
    else:
        return Vsource_max


t_start = 0
t_end   = 50
dt = 0.01

iter_times = int((t_end-t_start)/dt)

time_sequence = [0]
voltage_sequence = [initial_voltage]
current_sequence = [initial_current]

for i in range(iter_times):
    K_cur1 = dI(time_sequence[i],current_sequence[i],voltage_sequence[i])
    K_vol1 = dV(time_sequence[i],current_sequence[i],voltage_sequence[i])
    K_cur2 = dI(time_sequence[i]+dt/2,current_sequence[i]+dt/2*K_cur1,voltage_sequence[i]+dt/2*K_vol1)
    K_vol2 = dV(time_sequence[i]+dt/2,current_sequence[i]+dt/2*K_cur1,voltage_sequence[i]+dt/2*K_vol1)
    K_cur3 = dI(time_sequence[i]+dt/2,current_sequence[i]+dt/2*K_cur2,voltage_sequence[i]+dt/2*K_vol2)
    K_vol3 = dV(time_sequence[i]+dt/2,current_sequence[i]+dt/2*K_cur2,voltage_sequence[i]+dt/2*K_vol2)
    K_cur4 = dI(time_sequence[i]+dt,current_sequence[i]+dt*K_cur3,voltage_sequence[i]+dt*K_vol3)
    K_vol4 = dV(time_sequence[i]+dt,current_sequence[i]+dt*K_cur3,voltage_sequence[i]+dt*K_vol3)
    current_sequence.append(current_sequence[i] + dt/6*(K_cur1+2*K_cur2+2*K_cur3+K_cur4))
    voltage_sequence.append(voltage_sequence[i] + dt/6*(K_vol1+2*K_vol2+2*K_vol3+K_vol4))
    time_sequence.append(time_sequence[i] + dt)

plt.plot(time_sequence,voltage_sequence , label = 'Output')
plt.plot(time_sequence,[Vin(t) for t in time_sequence], label = 'Source')
plt.xlabel('Time')
plt.ylabel('Voltage')
plt.legend()
plt.show()

