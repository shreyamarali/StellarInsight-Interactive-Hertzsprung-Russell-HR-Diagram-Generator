import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("stars.csv")

df.columns = df.columns.str.strip()
df = df[(df["Temperature (K)"] > 0) & (df["Luminosity(L/Lo)"] > 0)]

plt.figure(figsize=(8, 6))
plt.scatter(df["Temperature (K)"], df["Luminosity(L/Lo)"], s=10, alpha=0.6)

plt.xscale("log")
plt.yscale("log")
plt.gca().invert_xaxis()

plt.xlabel("Surface Temperature (K)")
plt.ylabel("Luminosity ")
plt.title("Hertzsprung–Russell Diagram ( Star Dataset)")

plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.show()
