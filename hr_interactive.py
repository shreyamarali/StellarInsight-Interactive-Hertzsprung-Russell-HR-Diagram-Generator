import pandas as pd
import plotly.express as px

df = pd.read_csv("stars.csv")
df.columns = df.columns.str.strip()
df = df[(df["Temperature (K)"] > 0) & (df["Luminosity(L/Lo)"] > 0)]

star_type_map = {
    0: "Brown Dwarf",
    1: "Red Dwarf",
    2: "White Dwarf",
    3: "Main Sequence",
    4: "Supergiant",
    5: "Hypergiant"
}

df["Star type name"] = df["Star type"].map(star_type_map)

fig = px.scatter(
    df,
    x="Temperature (K)",
    y="Luminosity(L/Lo)",
    color="Star type name",
    symbol="Spectral Class",
    hover_data=[
        "Temperature (K)",
        "Luminosity(L/Lo)",
        "Radius(R/Ro)",
        "Absolute magnitude(Mv)",
        "Star type name",
        "Star color",
        "Spectral Class"
    ],
    title="Interactive Hertzsprung–Russell Diagram (Star Dataset)"
)

fig.update_xaxes(type="log", autorange="reversed", title="Surface Temperature (K)")
fig.update_yaxes(type="log", title="Luminosity ")

fig.show()
