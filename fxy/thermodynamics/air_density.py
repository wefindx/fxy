from sympy import symbols
from sympy.functions.elementary.piecewise import Piecewise
from scipy import constants as const

# air density based on altitude
# https://en.wikipedia.org/w/index.php?title=Density_of_air&oldid=862508599#Altitude

h = symbols('elevation') # meters above surface

# http://www.physicalgeography.net/fundamentals/7b.html
#
# Troposphere
# 11000: [15, -55] = 70/11000 = 0.0065
#
# Stratosphere:
#     30000: [-55, -3] = -52/30000 = -0.0017
#
# Mesosphere:
#     24000: [-3, -93] = 90/24000 = 0.00375
#
# Thermosphere:
#     10000: [-93, -45] = -48/10000. = -0.0048
#

standard_values = {
    'standard_sea_level_pressure': const.atm,
    'standard_sea_level_temperature': const.zero_Celsius+15.0,
    'earth_surface_gravitational_acceleration': const.g,
    'temperature_lapse_rate': 0.0065, # K/m
    'universal_gas_constant': const.R,
    'molar_mass_of_dry_air': 0.0289644 # Kg/mol at sea, 15'C.
}

p0, T0, g, L, R, M = symbols(','.join(standard_values.keys()))

# Lapse rates by height.
L_atmosphere = Piecewise(
    (L, h <=11000),
    (0, h <=20000),
    (-0.0017, h <=50000),
    (0, h <=55000),
    (0.00375, h <=80000),
    (0, h <=90000),
    (-0.0048, h<=1000000)
)

# TODO: To multiply by lapse rates, to avoid this ugly expressions
T_troposphere = (T0 - L*h).subs(standard_values)
T_tropopause = T_troposphere.subs(dict(standard_values,**{'elevation': 11000}))
T_stratosphere = T_tropopause + 0.0017*(h-20000)
T_stratopause = T_stratosphere.subs(dict(standard_values, **{'elevation': 50000}))
T_mesosphere = T_stratopause - 0.00375*(h-55000)
T_mesopause = T_mesosphere.subs(dict(standard_values, **{'elevation': 80000}))
T_thermosphere = T_mesopause + 0.0048*(h-90000)

# Temperature by height.
T_atmospehre = Piecewise(
    (T_troposphere, h <=11000),
    (T_tropopause, h <=20000),
    (T_stratosphere, h <=50000),
    (T_stratopause, h <=55000),
    (T_mesosphere, h <=80000),
    (T_mesopause, h <=90000),
    (T_thermosphere, h<=1000000)
)

# P_atmosphere = (p0)*(1-(L*h)/(T0))**((g*M)/(R*L))
P_atmosphere = (p0)*(1-(L_atmosphere.subs({'elevation': h}))/(T0))**((g*M)/(R*L_atmosphere.subs({'elevation': h})))

D_atmosphere = (P_atmosphere*M)/(R*T_atmospehre)

T_standard = T_atmospehre.subs(standard_values)
P_standard = P_atmosphere.subs(standard_values)

# air density by height
D_standard = D_atmosphere.subs(standard_values)
