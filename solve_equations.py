import numpy as np
import matplotlib.pyplot as plt

# Data från uppgiften
L1 = 45*1000
L2 = 72*1000
L3 = 40*1000
L4 = 100*1000

zb = 372
zc = 290

a1 = 75
a2 = 89
a3 = 45
a4 = 93

g=9.81
f = 0.02



# För att kunna köra programmet behöver du installera numpy och matplotlib.
# Om du inte har dessa installerade, kan du göra det med:
#
# pip install numpy matplotlib
#
# Detta kör du i terminalen eller kommandoprompten.

# Parametrar från Möbius
d1 = 14                     # Diameter på rör 1 i meter
za = 425                    # Höjd på punkt A i meter
V3 = 75                     # Volymflöde i rör 3 i m³/s

#Parameter för programmet
solver_iterations = 25







d3 = d1/2
w3 = 4*V3/(np.pi*d3*d3)






def F(w1, w2, w4, d2, d4, zd):
    return np.array([
        zb - za + (2.5 + 2*f*L1/d1 + a1)*w1**2/(2*g),
        zd - zb + (2.0 + 2*f*L2/d2 + a2)*w2**2/(2*g),
        zd - zc + (2.0 + 2*f*L3/d3 + a3)*w3**2/(2*g),
        0  - zd + (0.5 + 2*f*L4/d4 + a4)*w4**2/(2*g),
        
        
        d2**2*w2 + d3**2*w3 - d4**2*w4,
        d1**2*w1 - d2**2*w2
    ])
def J(w1, w2, w4, d2, d4, zd):
    row1_dw1 = (2.5 + 2*f*L1/d1 + a1) * w1 / g
    row2_dw2 = (2.0 + 2*f*L2/d2 + a2) * w2 / g
    row4_dw4 = (0.5 + 2*f*L4/d4 + a4) * w4 / g
    
    row2_dd2 = -f*L2 * w2**2 / (g * d2**2)
    row4_dd4 = -f*L4 * w4**2 / (g * d4**2)

    return np.array([
        [row1_dw1, 0, 0, 0, 0, 0],
        [0, row2_dw2, 0, row2_dd2, 0, 1],
        [0, 0, 0, 0, 0, 1],
        [0, 0, row4_dw4, 0, row4_dd4, -1],
        [0, d2**2, -d4**2, 2*d2*w2, -2*d4*w4, 0],
        [d1**2, -d2**2, 0, -2*d2*w2, 0, 0]
    ])




# Startgissning. Alla hastigheter, diametrar och höjd gissas vara lika stora som givna väreden i uppgiften.
x = np.array([w3, w3, w3, d1, d1, za])

# Spara lösningar för varje iteration
x_history = [x.copy()]






# Iteration
labels = ["w1", "w2", "w4", "d2", "d4", "zd"]
for i in range(solver_iterations):
    J_eval = J(x[0], x[1], x[2], x[3], x[4], x[5])
    F_eval = F(x[0], x[1], x[2], x[3], x[4], x[5])
    dx = np.linalg.solve(J_eval, F_eval)
    x = x - dx
    x_history.append(x.copy())
    print("-" * 20, "Iteration", i+1, "Error:", np.linalg.norm(dx), "-" * 20)
    print("Lösning:")
    for label, value in zip(labels, x):
        print(f"{label}: {value:.6f}")









# Konvertera till numpy-array för enklare hantering
x_history = np.array(x_history)

# Plot
plt.figure(figsize=(10, 6))
for idx, label in enumerate(labels):
    plt.plot(x_history[:, idx], marker='o', label=label)
    for i, y in enumerate(x_history[:, idx]):
        plt.text(i, y, f"{y:.2f}", fontsize=8, ha='right', va='bottom', rotation=30)
plt.xlabel("Iteration")
plt.ylabel("Värde")
plt.title("Utveckling av variabler x(n) per iteration")
plt.legend()
plt.grid(True)
plt.tight_layout()


print("\nSlutgiltiga värden efter iterationer:")

V1 = np.pi*d1**2*x[0]/4
V4 = np.pi*x[4]**2*x[2]/4
d2 = x[3]
d4 = x[4]

print(f"Beräknat volymflöde V1: {V1:.4f} m³/s")
print(f"Beräknad diameter d2: {d2:.4f} m")
print(f"Beräknat volymflöde V4: {V4:.4f} m³/s")
print(f"Beräknad diameter d4: {d4:.4f} m")

plt.show()