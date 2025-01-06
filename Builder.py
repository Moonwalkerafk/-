# позволяет поэтапно строить сложные объекты


class Car:
    def __init__(self):
        self.engine = None
        self.body = None
        self.wheels = None

    def __str__(self):
        return f"Car with {self.engine}, {self.body}, and {self.wheels} wheels."


class CarBuilder:
    def __init__(self):
        self.car = Car()

    def build_engine(self, engine_type):
        self.car.engine = engine_type
        return self

    def build_body(self, body_type):
        self.car.body = body_type
        return self

    def build_wheels(self, wheel_count):
        self.car.wheels = wheel_count
        return self

    def get_result(self):
        return self.car


builder = CarBuilder()
car = builder.build_engine("V8 Engine").build_body("Sedan Body").build_wheels(4).get_result()
print(car)
