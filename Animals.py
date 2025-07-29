class Animal:
    def __init__(self, type, x, y, forward_power, gender):
        self.type = type
        self.x = x
        self.y = y
        self.forward_power = forward_power
        self.gender = gender

    def move(self, dx=0, dy=0, area_size=500):
        if dx == dy:
            raise ValueError("Aynı anda x ve y eksininde hareket edilemez.")  
        
        new_x = self.x + dx * self.forward_power
        new_y = self.y + dy * self.forward_power

        new_x = max(0, min(area_size - 1, new_x))
        new_y = max(0, min(area_size - 1, new_y))

        self.x = new_x
        self.y = new_y

    def get_location(self):
        return self.x, self.y

class Sheep(Animal):
    def __init__(self, x, y, gender):
        super().__init__("Sheep", x, y, forward_power=2, gender=gender)
        self.code = 0
        self.alive = True

class Wolf(Animal):
    def __init__(self, x, y, gender):
        super().__init__("Wolf", x, y, forward_power=3, gender=gender)
        self.code = 1
        self.alive = True

class Cow(Animal):
    def __init__(self, x, y, gender):
        super().__init__("Cow", x, y, forward_power=2, gender=gender)
        self.code = 2  
        self.alive = True

class Hen(Animal):
    def __init__(self, x, y):
        super().__init__("Hen", x, y, forward_power=1, gender="Female")
        self.code = 3
        self.alive = True

class Cockerel(Animal):
    def __init__(self, x, y):
        super().__init__("Cockerel", x, y, forward_power=1, gender="Male")
        self.code = 4
        self.alive = True

class Lion(Animal):
    def __init__(self, x, y, gender):
        super().__init__("Lion", x, y, forward_power=4, gender=gender)
        self.code = 5
        self.alive = True

class Hunter(Animal):
    def __init__(self, x, y):
        super().__init__("Hunter", x, y, forward_power=1, gender="Male")
        self.code = 6
        self.alive = True