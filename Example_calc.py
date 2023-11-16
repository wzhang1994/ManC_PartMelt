"""
For typical values of [Asimow et al., 1999, 2001] F 7.2%, Po 2.75 GPa, Pf 0.2 GPa, and rc = 2880 kg m3, equation (A9) gives hc  6.5 km.
"""
import mean_F_calc

print("This is a example from Afonso et al., 2008 G3") 
F_mean=0.072
rho_crust=2880 # density of oceanic crust in kg/m3
g=9.8   # accelration due to gravity
Po=2.75 # pressure at intersection of solidus (GPa)
Pf=0.2  # pressure at which melting stops (GPa)
hc= F_mean * (Po-Pf) / rho_crust / g  * 10**6
print("The thickness of oceanic crust (km):",hc)


print("\nCalculating by funcition mean_F_calc......")
F_mean = mean_F_calc.F_mean_cal_A08_ex(hc)   # refers to Asimow et al., 1999, 2001
F_mean = mean_F_calc.F_mean_cal_A08_FA1(hc)  # prefer model from Afonso et al., (2008)