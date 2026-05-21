import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# =========================
# PART 1: HERTZSPRUNG–RUSSELL DIAGRAM
# =========================

data = {
    "Star": ["Sun", "Sirius", "Betelgeuse", "Rigel", "Proxima Centauri",
             "White Dwarf", "Red Giant", "Blue Giant"],
    "Temperature": [5778, 9940, 3500, 11000, 3050, 25000, 4000, 20000],
    "Luminosity": [1, 25, 120000, 120000, 0.0017, 0.01, 1000, 20000]
}

df = pd.DataFrame(data)

plt.figure(figsize=(8, 6))
plt.scatter(df["Temperature"], df["Luminosity"], s=120)

for i in range(len(df)):
    plt.text(df["Temperature"][i]*1.05, df["Luminosity"][i], df["Star"][i], fontsize=9)

plt.xscale("log")
plt.yscale("log")
plt.gca().invert_xaxis()

plt.xlabel("Surface Temperature (K)")
plt.ylabel("Luminosity (L / L☉)")
plt.title("Hertzsprung–Russell Diagram")

plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.show()


# =========================
# PART 2: MASS–LUMINOSITY RELATION
# =========================

mass = np.array([0.2, 0.5, 1, 2, 5, 10])     # in solar masses
luminosity_ml = mass ** 3.5                 # L ∝ M^3.5

plt.figure(figsize=(7, 5))
plt.plot(mass, luminosity_ml, 'o-', label=r'$L \propto M^{3.5}$')

plt.xscale("log")
plt.yscale("log")

plt.xlabel("Mass (M / M)")
plt.ylabel("Luminosity (L / L☉)")
plt.title("Mass–Luminosity Relation for Main Sequence Stars")

plt.grid(True, which="both", linestyle="--")
plt.legend()
plt.show()
