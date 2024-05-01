quadrant_id = {
	( 1,  1): "q1",
	(-1,  1): "q2",
	(-1, -1): "q3",
	( 1, -1): "q4",
	( 0,  1): "x-Axis",
	( 0, -1): "x-Axis",
	( 1,  0): "y-Axis",
	(-1,  0): "y-Axis",
	( 0,  0): "center"
}

octant_id = {
	( 1,  1,  1): "o0",
	(-1,  1,  1): "o1",
	(-1, -1,  1): "o2",
	( 1, -1,  1): "o3",
	( 1, -1, -1): "o4",
	(-1, -1, -1): "o5",
	(-1,  1, -1): "o6",
	( 1,  1, -1): "o7",	
	( 0,  1, 0): "x-Axis",
	( 0, -1, 0): "x-Axis",
	( 1,  0,  0): "y-Axis",
	(-1,  0,  0): "y-Axis",
	( 0,  0,  1): "z-Axis",
	( 0,  0, -1): "z-Axis",
	( 0,  0,  0): "center"
}

def sign_reduction(values: tuple[float,...]) -> tuple[float,...]:
	"""
 	Used for reducing coordinates down to their sign values represented as -1 for negative, 0 for neutral, and 1 for positive.
	"""
	result = [1 if value > 0 else -1 if value < 0 else 0 for value in values]
	return tuple(result)