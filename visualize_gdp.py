from clouddrift.datasets import gdp1h
from clouddrift.ragged import subset
from clouddrift.plotting import plot_ragged
import matplotlib.pyplot as plt
import numpy as np

# Connect to the GDP hourly dataset
ds = gdp1h()

# Select the first 10 drifter IDs
ids = ds.id[:10].values

# Extract the complete trajectories for these 10 drifters
small_ds = subset(
    ds,
    {"id": ids},
    row_dim_name="traj"
).load()

print("Number of trajectories:", small_ds.sizes["traj"])
print("Number of observations:", small_ds.sizes["obs"])

# Create the figure
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the trajectories
plot_ragged(
    ax,
    small_ds.lon,
    small_ds.lat,
    small_ds.rowsize,
    colors=np.arange(len(small_ds.rowsize))
)

ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
ax.set_title("Global Drifter Program - Sample Trajectories")

ax.grid(True)

plt.savefig(
    "sample_trajectories.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
