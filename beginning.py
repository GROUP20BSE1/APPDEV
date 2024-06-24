
import geopandas as gpd
from shapely.geometry import Point, Polygon, mapping
import pyproj

stops_gdf = gpd.read_file('data/stops.shp')  # Assuming 'stops.shp' is the filename
routes_gdf = gpd.read_file('data/routes.shp')  # Assuming 'routes.shp' is the filename


stop_by_code = stops_gdf[stops_gdf['stop_code'] == 50117]
stop_name = stop_by_code['stop_name'].values[0]  # Assuming a unique stop name
print(f"Stop name for stop_code 50117: {stop_name}")

unique_routes = routes_gdf['route_number'].unique()
print("Unique transit route numbers:", sorted(unique_routes))  # Sort for clarity

wkt_string = "POINT (-73.587519 45.504840)"  # Replace with actual WKT if different

wgs84 = pyproj. CRS.from_epsg(4326)  # WGS84 projection
mtm8 = pyproj. CRS.from_epsg(32188)  # Target projection (NAD 1983 MTM 8)
transformer = pyproj.Transformer.from_crs(wgs84, mtm8)
point = Point(*transformer.transform(float(wkt_string.split()[1]), float(wkt_string.split()[2])))
