from .error import ErrorMessage
from .trigonometry import quadrant_id, octant_id, sign_reduction

class Vector:
	@staticmethod
	def vectorize(vec_type, coords: tuple[tuple[float,float], ...]):
		result = [vec_type(*coord) for coord in coords]
		return tuple(result)

	def __add__(self, other):
		if type(self) == type(other):
			result = [self.value[i] + other.value[i] for i in range(len(self.value))]
			return type(self)(*result)
		else:
			raise TypeError(ErrorMessage.operator_overload(self,other, "+"))
	
	def __sub__(self, other):
		if type(self) == type(other):
			result = [self.value[i] - other.value[i] for i in range(len(self.value))]
			return type(self)(*result)
		else:
			raise TypeError(ErrorMessage.operator_overload(self,other, "-"))
	
	def __mul__(self, other):
		if type(self) == type(other):
			result = [self.value[i] * other.value[i] for i in range(len(self.value))]
			return type(self)(*result)
		else:
			raise TypeError(ErrorMessage.operator_overload(self,other, "*"))
	
	def __truediv__(self, other):
		if type(self) == type(other):
			result = [self.value[i] / other.value[i] for i in range(len(self.value))]
			return type(self)(*result)
		else:
			raise TypeError(ErrorMessage.operator_overload(self,other, "/"))
	
	def __eq__(self, other):
		if type(self) == type(other):
			for i in range(len(self.value)):
				if self.value[i] != other.value[i]:
					return False
			return True
		else:
			return False

class Vec2(Vector):
	def __init__(self, x: float, y: float):
		super().__init__()
		self._x = x
		self._y = y
	
	@property
	def x(self) -> float:
		return self._x
	
	@x.setter
	def x(self, value: float):
		self._x = value
	
	@property
	def y(self) -> float:
		return self._y
	
	@y.setter
	def y(self, value: float):
		self._y = value
	
	@property
	def value(self):
		return (self._x, self._y)

	@property
	def quadrant(self):
		sign_values = sign_reduction((self._x, self._y))
		return quadrant_id[sign_values]

class Vec3(Vector):
	def __init__(self, x: float, y: float, z: float):
		super().__init__()
		self._x = x
		self._y = y
		self._z = z

	@property
	def x(self) -> float:
		return self._x
	
	@x.setter
	def x(self, value: float):
		self._x = value
	
	@property
	def y(self) -> float:
		return self._y
	
	@y.setter
	def y(self, value: float):
		self._y = value

	@property
	def z(self) -> float:
		return self._z

	@z.setter
	def z(self, value: float):
		self._z = value
	
	@property
	def value(self):
		return (self._x, self._y, self._z)

	@property
	def octant(self):
		sign_values = sign_reduction((self._x, self._y,self._z))
		return octant_id[sign_values]
