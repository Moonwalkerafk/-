#предоставляет абстракцию для создания объектов.

class Product:
    def action(self):
        raise NotImplementedError("Action method not implemented.")


class ConcreteProductA(Product):
    def action(self):
        return "Action from ConcreteProductA"


class ConcreteProductB(Product):
    def action(self):
        return "Action from ConcreteProductB"


class Creator:
    def factory_method(self):
        raise NotImplementedError("Factory method should be overridden.")


class ConcreteCreatorA(Creator):
    def factory_method(self):
        return ConcreteProductA()


class ConcreteCreatorB(Creator):
    def factory_method(self):
        return ConcreteProductB()


creator_a = ConcreteCreatorA()
product_a = creator_a.factory_method()
print(product_a.action())

creator_b = ConcreteCreatorB()
product_b = creator_b.factory_method()
print(product_b.action())
