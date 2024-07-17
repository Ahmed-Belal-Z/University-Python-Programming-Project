#This is code to implement a container:

class Container:
    def __init__(self, ID, weight, container_type=None, station_id=None):

        self.ID = ID
        self.weight = weight
        self.type = container_type if container_type else self.creating_container()
        self.is_refrigerated = 'R' in str(weight)
        self.is_liquid = 'L' in str(weight)
        self.station_id = station_id

    def double_consumption(self) -> float:

        return 0.0

    def boolean_equals(self, other) -> bool:

        if isinstance(other, Container):
            return self.ID == other.ID and self.weight == other.weight and type(self) == type(other)
        return False

    def creating_container(self):

        weight_str = str(self.weight)
        if weight_str[-1] == 'R':
            container_type = 'RefrigeratedContainer'
        elif weight_str[-1] == 'L':
            container_type = 'LiquidContainer'
        elif int(weight_str) > 3000:
            container_type = 'HeavyContainer'
        else:
            container_type = 'NormalContainer'
            return bool(container_type)

        def __str__(self):

            return (f"Container :\n[ Container ID: {self.ID}\nContainer Weight: {self.weight}\nContainer type : {self.type}\nRefrigerated Container : {self.is_refrigerated}\nLiquid Container  : {self.is_liquid}\nStation id : {self.station_id} ]")


class NormalContainer(Container):
    def __init__(self, ID, weight):

        super().__init__(ID, weight)

    def double_consumption(self) -> float:

        return 2.5 * self.weight


class HeavyContainer(Container):
    def __init__(self, ID, weight):

        super().__init__(ID, weight)

    def double_consumption(self) -> float:

        return 3.0 * self.weight


class RefrigeratedContainer(HeavyContainer):
    def __init__(self, ID, weight):

        super().__init__(ID, weight)

    def double_consumption(self) -> float:

        return 5.0 * self.weight



class LiquidContainer(HeavyContainer):
    def __init__(self, ID, weight):

        super().__init__(ID, weight)
