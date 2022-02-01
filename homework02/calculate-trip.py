import json
import math

mars_radius = 3389.5    # km

composition_sample_time = {
    "stony" : 1,
    "iron" : 2,
    "stony-iron" : 3
}

# Convert a json file to a dictionary
def json_to_dict(filename):
    f = open(filename)
    data = json.load(f)
    f.close()
    return data

# Calculate distance between two points on Mars using the great-circle distance algorithm
def calc_gcd(latitude_1, longitude_1, latitude_2, longitude_2):
    lat1, lon1, lat2, lon2 = map( math.radians, [latitude_1, longitude_1, latitude_2, longitude_2] )
    d_sigma = math.acos( math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(abs(lon1-lon2)))
    return ( mars_radius * d_sigma )

def main():
    data = json_to_dict("data.json")
    # Starting point
    curr_lat = 16.0
    curr_lon = 82.0
    total_time = 0.0
    # Iterate through sites
    for i in range(len(data['sites'])):
        # Find the next point to travel to
        next_site = data['sites'][i]
        next_lat = next_site['latitude']
        next_lon = next_site['longitude']
        next_comp = next_site['composition']

        # Calculate distance
        dist = calc_gcd(curr_lat, curr_lon, next_lat, next_lon)

        # Calculate time spent
        travel_time = round(dist / 10.0, 2)
        sample_time = composition_sample_time[next_comp]

        # Format report
        leg_info = "leg = " + str(i + 1) + ","
        travel_time_info = "time to travel = " + str(travel_time) + " hr,"
        sample_time_info = "time to sample = " + str(sample_time) + " hr"

        # Print report
        print(leg_info, travel_time_info, sample_time_info)

        # Update the current point
        curr_lat = next_lat
        curr_lon = next_lon

        # Update total time spent so far
        total_time += travel_time + sample_time

    # Format and print summary info
    break_line = "=" * 58
    print(break_line)
    print("number of legs = " + str(len(data['sites'])) + ", total time elapsed = " + str(round(total_time, 2)) + " hr")

main()
