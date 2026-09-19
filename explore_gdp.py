from clouddrift.datasets import gdp1h
from clouddrift.ragged import subset

# Connect to the GDP dataset
ds = gdp1h()

print("Original dataset:")
print(ds.sizes)

# Temporary test region only - not the final Region R
region = subset(
    ds,
    {
        "lat": (21, 31),
        "lon": (-98, -78)
    },
    row_dim_name="traj"
)

print("\nRegion dataset:")
print(region.sizes)

print("\nNumber of trajectories:")
print(region.sizes["traj"])

print("\nNumber of observations:")
print(region.sizes["obs"])