# Givna parametrar
t_kond_steam = 95
t2_heatpump = 7
η = 0.77

# Antagande
m_steam = 1000


# Entalpier
# Ångkraftverk
ha_steam = 398  # kJ/kg     
hb_steam = 398.0823006  # kJ/kg
hc_steam = 3400  # kJ/kg
hd_steam_isentropic = 2425  # kJ/kg
# ha_steam = 389  # kJ/kg     
# hb_steam = 389  # kJ/kg
# hc_steam = 3400  # kJ/kg
# hd_steam_isentropic = 2425  # kJ/kg
hd_steam = hc_steam - η * (hc_steam - hd_steam_isentropic)  # kJ/kg

# Värmepump
# ha_heatpump = 256.5  # kJ/kg
# hb_heatpump = 256.5  # kJ/kg
# hc_heatpump_isentrpoic = 2800  # kJ/kg
# hd_heatpump = 411.19  # kJ/kg
ha_heatpump = 256.5  # kJ/kg
hb_heatpump = 256.5  # kJ/kg
hc_heatpump_isentrpoic = 440  # kJ/kg
hd_heatpump = 411.19  # kJ/kg
hc_heatpump = (hc_heatpump_isentrpoic - hd_heatpump) / η + hd_heatpump  # kJ/kg



# Beräkningar
# Turbinarbete/kompressorarbete
ε_steam =  hc_steam - hd_steam  # kJ/kg
ε_heatpump =  hc_heatpump - hd_heatpump  # kJ/kg

#Massflöde värmepump
m_heatpump = m_steam * ε_steam / ε_heatpump  # kg/s


# Värmeutbyte
# hc_heatpump = hc_heatpump_isentrpoic - ε_heatpump*η  # kJ/kg

q1_steam = hc_steam - hb_steam  # kJ/kg
q2_steam = hd_steam - ha_steam
q1_heatpump = hc_heatpump - hb_heatpump  # kJ/kg
q2_heatpump = hd_heatpump - ha_heatpump  # kJ/kg

# Effektutbyte
E_steam =       ε_steam *   m_steam  # kJ/s
Q1_steam =      q1_steam *  m_steam  # kJ/s
Q2_steam =      q2_steam *  m_steam  # kJ/s
E_heatpump =    ε_heatpump *  m_heatpump  # kJ/s
Q1_heatpump =   q1_heatpump * m_heatpump  # kJ/s
Q2_heatpump =   q2_heatpump * m_heatpump  # kJ/s

#Sökt:
COP1_total = 0          + (Q2_steam + Q1_heatpump) / (Q1_steam)   # Total COP
ηt_steam = 0            + E_steam / Q1_steam                       # Termisk verkningsgrad för ångkraftverk
COP1_heatpump = 0       + 0 * Q1_heatpump / E_heatpump    + (hc_heatpump - hb_heatpump) / (hc_heatpump - hd_heatpump)                          # COP för värmepump
ratio_heat_steam = 0    + 100 * Q2_steam / (Q2_steam + Q1_heatpump)                   # Förhållande mellan värme från ångkraftverk och värmepump
ratio_heat_heatpump = 0 + 100 * Q1_heatpump / (Q2_steam + Q1_heatpump)                # Förhållande mellan värme från värmepump och ångkraftverk

print()
print()
print(f"COP1_total: {COP1_total:.4f}")
print(f"ηt_steam: {ηt_steam:.4f}")
print(f"COP1_heatpump: {COP1_heatpump:.4f}")
print(f"ratio_heat_steam: {ratio_heat_steam:.4f}")
print(f"ratio_heat_heatpump: {ratio_heat_heatpump:.4f}")
print()
print()

# Skriv ut alla variabler och deras värden
print("Alla variabler:")
for name, value in sorted(locals().items()):
    if not name.startswith("__") and not callable(value):
        print(f"{name}: {value}")



# 1.7722297
# 0.2429425