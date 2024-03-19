class Circle:
    def __init__(self, radius, area):
        self._radius = radius
        self.area = area

    @property
    def radius(self):
        """ Get radius """
        return self._radius

    @radius.setter
    def radius(self, value):
        """ Set radius """
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")

    @radius.deleter
    def radius(self):
        """ Delete radius """
        del self._radius

# Instanciating a circle with radius 5
c = Circle(5, 10)
# Getting instantiated circle radius
print(f"The radius of c is: {c.radius}") # 5
# Setting instantiated circle radius
c.radius = 10
# Getting new radius value
print(f"The new radius of c is: {c.radius}") # 10
# Printing all attributes of c
print(f"Those are the attributes of c: {c.__dict__}")
# Deleting radius attribute
del c.radius
# Checking if radius attribute is deleted
print(f"The radius attribute has been deleted, now c has these attributes: {c.__dict__}")
print("If you try to print c.radius, it will raise the AttributeError exception: 'Circle' object has no attribute '_radius'. Did you mean: 'radius'?")
