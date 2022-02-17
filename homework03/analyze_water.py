import logging
logging.basicConfig(level=logging.DEBUG, format=f'%(levelname)s: %(message)s')
import math
import json

# calculate turbidity
def calc_turbidity(calibration_constant, detector_current):
    """
def calc_turbidity - calculates the turbidity from the calibration costant multiplied by the detector current
    """   
 # T = a0 * I90
    # a0 = Calibration constant; I90 = Ninety degree detector current
    return calibration_constant * detector_current

# calculate minimum time to fall below threshold
def calc_thresh_time(calibration_constant, detector_current):
    """
def calc_thresh_time - calculates the mininum time to fall below the threshold
contains the following variables:     
	Ts > T0((1-d)**b)
	Ts/T0 > (1-d)**b
        log(Ts/T0) > b log(1-d)
        log(Ts/T0) / log(1-d) > b
        Ts = Turbidity threshold for safe water; T0 = Current turbidity;
        d = decay factor per hour; b = hours elapsed
     """
    turb_thresh = 1.0
    curr_turb = calc_turbidity(calibration_constant, detector_current)
    decay = 0.02

    return math.log(turb_thresh / curr_turb) / math.log(1 - decay)

# Convert a json file to a dictionary list
def json_to_dict_list(filename):
    f = open(filename)
    data = json.load(f)
    f.close()
    return data

def main():

    dict = json_to_dict_list("turbidity_data.json")
    data = dict["turbidity_data"]
    # sort the dict list by reverse datetime string 
    # such that data[0:5] will be the 5 most recent entries
    data = sorted(data, key = lambda x: x["datetime"], reverse=True)

    # amount of recent entries to consider in average
    n_recent_entries = 5
    avg_turbidity = 0.0
    recent_data = data[0:n_recent_entries]

    # calculate the average of the n most recent data points
    for data in recent_data:
        avg_turbidity += calc_turbidity(data["calibration_constant"], data["detector_current"])
    avg_turbidity /= len(recent_data)

    # print average
    print("Average turbidity based on most recent", n_recent_entries, "entries = ", round(avg_turbidity, 4), "NTU")

    # safe turbidity threshold is 1.0 NTU, anything above is unsafe
    if (avg_turbidity > 1.0):
        # unsafe case
        logging.warning("Turbidity is above threshold for safe use")
    else:
        # safe case
        logging.info("Turbidity is below threshold for safe use")

    # calculate and print time to fall below threshold
    time_to_safety = calc_thresh_time(data["calibration_constant"], data["detector_current"])
    print("Minimum time required to return below a safe threshold =", round(time_to_safety,2), "hours")

    return 0

main()
