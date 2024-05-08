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

		elif type(other) == list or type(other) == tuple:
			result = [self.value[i] + other[i] for i in range(len(self.value))]
			return type(self)(*result)

		elif type(other) == float or type(other) == int:
			result = [self.value[i] + other for i in range(len(self.value))]
			return type(self)(*result)

		else:
			raise TypeError(ErrorMessage.operator_overload(self,other, "+"))
	
	def __sub__(self, other):
		if type(self) == type(other):
			result = [self.value[i] - other.value[i] for i in range(len(self.value))]
			return type(self)(*result)

		elif type(other) == list or type(other) == tuple:
			result = [self.value[i] - other[i] for i in range(len(self.value))]
			return type(self)(*result)

		elif type(other) == float or type(other) == int:
			result = [self.value[i] - other for i in range(len(self.value))]
			return type(self)(*result)

		else:
			raise TypeError(ErrorMessage.operator_overload(self,other, "-"))
	
	def __mul__(self, other):
		if type(self) == type(other):
			result = [self.value[i] * other.value[i] for i in range(len(self.value))]
			return type(self)(*result)

		elif type(other) == list or type(other) == tuple:
			result = [self.value[i] * other[i] for i in range(len(self.value))]
			return type(self)(*result)

		elif type(other) == float or type(other) == int:
			result = [self.value[i] * other for i in range(len(self.value))]
			return type(self)(*result)

		else:
			raise TypeError(ErrorMessage.operator_overload(self,other, "*"))
	
	def __truediv__(self, other):
		if type(self) == type(other) or type(other) == list or type(other) == tuple:
			result = [self.value[i] / other.value[i] for i in range(len(self.value))]
			return type(self)(*result)

		elif type(other) == list or type(other) == tuple:
			result = [self.value[i] / other[i] for i in range(len(self.value))]
			return type(self)(*result)

		elif type(other) == float or type(other) == int:
			result = [self.value[i] / other for i in range(len(self.value))]
			return type(self)(*result)

		else:
			raise TypeError(ErrorMessage.operator_overload(self,other, "/"))
	
	def __eq__(self, other):
		if type(self) == type(other) or type(other) == list or type(other) == tuple:
			for i in range(len(self.value)):
				if self.value[i] != other.value[i]:
					return False
			return True

		elif type(other) == list or type(other) == tuple:
			for i in range(len(self.value)):
				if self.value[i] != other[i]:
					return False
			return True

		elif type(other) == float or type(other) == int:
			for i in range(len(self.value)):
				if self.value[i] != other:
					return False
			return True

		else:
			return False

	def __neg__(self):
		return type(self)(-self.x, -self.y)

	def __pos__(self):
		return type(self)(self.x, self.y)

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
	def value(self) -> tuple[float, float]:
		return (self._x, self._y)

	@value.setter
	def value(self, value: tuple[float, float]):
		self._x = value[0]
		self._y = value[1]

	@property
	def quadrant(self) -> tuple[int, int]:
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
	def value(self) -> tuple[float, float, float]:
		return (self._x, self._y, self._z)

	@value.setter
	def value(self, value: tuple[float, float, float]):
		self._x = value[0]
		self._y = value[1]
		self._z = value[2]

	@property
	def octant(self) -> tuple[int, int, int]:
		sign_values = sign_reduction((self._x, self._y,self._z))
		return octant_id[sign_values]
