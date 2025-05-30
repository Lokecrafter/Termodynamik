import numpy as np

# Parametrar från Möbius
m_remote = 14
t_radiator_in = 52
t_water_out = 55


# Data från uppgiften
t_remote_in = 90
t_water_in = 12
m_water = 0.2 # kg/s
m_radiator = 1.5 # kg/s
kA_radiator = 3700 # W/K
c = 4.2 * 1000 # kJ/kg/K


# 35% varmvatten
# 65% radiator
m1 = m_remote * 0.35  # kg/s
m2 = m_remote * 0.65  # kg/s

η1_water = 0
η2_water = 0
# t_remote_out = 0


# Varmvattenväxlare
θ_water = t_remote_in - t_water_in  # K
Δ2_water = t_water_out - t_water_in  # K
Δ1_water = Δ2_water * m_water / m1  # K
ϑ1_water = θ_water - Δ1_water  # K
ϑ2_water = t_remote_in - t_water_out
ϑm_water = (ϑ1_water - ϑ2_water) / np.log(ϑ1_water/ϑ2_water)  # m³/s/K

Q_water = m_water * c * Δ2_water # kJ/s
print(f"Q_water: {Q_water:.5f} kJ/s")
Q_water = m1 * c * Δ1_water # kJ/s
print(f"Q_water: {Q_water:.5f} kJ/s")





# Radiatorväxlare
X = kA_radiator / (m2 * c)  # K/(kg/s)
Y = m2 / m_radiator
θ_radiator = t_remote_in - t_radiator_in  # K

Δ1_radiator = θ_radiator * (1 - np.exp(-X * (1 - Y))) / (1 - Y*np.exp(-X * (1 - Y)))  # K
Δ2_radiator = Δ1_radiator * m2 / m_radiator # K


# Fjärrvärmenätets uttemperatur
t1_out = t_remote_in - Δ1_water
t2_out = t_remote_in - Δ1_radiator

# Sökt:
kA_water = Q_water / ϑm_water
t_radiator_out = t_radiator_in + Δ2_radiator
t_remote_out = (t1_out * m1 + t2_out * m2) / m_remote  # K

# Snygg utskrift av sökta variabler
print("\n--- Sökta variabler ---")
print(f"kA_water:        {kA_water:.5f} W/K")
print(f"t_radiator_out:  {t_radiator_out:.5f} °C")
print(f"t_remote_out:    {t_remote_out:.5f} °C")