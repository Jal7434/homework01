from analyze_water import calc_turbidity, calc_thresh_time, main
import pytest
import math
def test_calc_turbidity():
	assert calc_turbidity(3, 5.2) == 3*5.2
	assert calc_turbidity(1.32, 3.22) == 1.32 * 3.22 
	assert isinstance(calc_turbidity(3.2,1),float) == True

def test_calc_thresh_time():
	assert calc_thresh_time(1.0,1.5) == (math.log(1.0/1.5)/math.log(1-0.02))
	assert calc_thresh_time(1.0,0.7) == (math.log(1.0/0.7)/math.log(1.0-0.02)) 
	assert isinstance(calc_thresh_time(1.0,1.1), float) == True

def test_calc_turbidity_exceptions():
	with pytest.raises(TypeError):
		calc_turbidity('2.2', '1.3')
	with pytest.raises(NameError):
		calc_turbidity(constant)
def test_calc_thresh_time_exceptions():
	with pytest.raises(TypeError):
		calc_thresh_time('0.4')
	with pytest.raises(NameError):
		calc_thresh_time(curr_turb) 
