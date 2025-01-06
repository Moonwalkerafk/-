#создает целые семейства объектов, не привязываясь к конкретным классам.


class AbstractChair:
    def sit(self):
        raise NotImplementedError("Sit method not implemented.")


class ModernChair(AbstractChair):
    def sit(self):
        return "Sitting on a modern chair."


class VictorianChair(AbstractChair):
    def sit(self):
        return "Sitting on a Victorian chair."


class AbstractSofa:
    def lie_down(self):
        raise NotImplementedError("Lie down method not implemented.")


class ModernSofa(AbstractSofa):
    def lie_down(self):
        return "Lying down on a modern sofa."


class VictorianSofa(AbstractSofa):
    def lie_down(self):
        return "Lying down on a Victorian sofa."


class FurnitureFactory:
    def create_chair(self):
        raise NotImplementedError("Create chair method not implemented.")

    def create_sofa(self):
        raise NotImplementedError("Create sofa method not implemented.")


class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return ModernChair()

    def create_sofa(self):
        return ModernSofa()


class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return VictorianChair()

    def create_sofa(self):
        return VictorianSofa()


modern_factory = ModernFurnitureFactory()
victorian_factory = VictorianFurnitureFactory()

modern_chair = modern_factory.create_chair()
victorian_chair = victorian_factory.create_chair()

print(modern_chair.sit())
print(victorian_chair.sit())
