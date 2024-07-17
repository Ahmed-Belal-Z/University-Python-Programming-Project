#Project that Simulates a Cargo Freight Cars management system.

import sys
sys.dontwritebytecode = True
from container import Container, NormalContainer, HeavyContainer, RefrigeratedContainer, LiquidContainer
from station import Station
from freightcar import FreightCar


class Main():

    # Test Case 1:
    print("Test Case 1:")
    print(Station.create_station(0, 40, 50))

    # Test Case 2:

    print("Test Case 2:")

    station3 = Station.create_station(3, 0.0, 0.0)
    freight_car0 = FreightCar(0, station3, 10000, 10, 5, 3, 2, 2.0)
    container1 = NormalContainer(1, 2500)
    container2 = HeavyContainer(2, 4000)
    container3 = RefrigeratedContainer(3, 4500)
    freight_car0.containers = {container1, container2, container3}
    freight_car0.unload_container(1, station3)

    print(freight_car0)

    # Test Case 3:
    print("Test case 3:")
    container_1 = Container(0,'NormalContainer',500)
    container_2 = Container(1,"HeavyContainer", 3500)
    print(container_1)
    print(container_2)

    #Test Case 4:
    print("Test Case 4:")
    Freight_Car = FreightCar(0, Station(
        2, 'Station_2', ()), 14000, 10, 5, 4, 1, 0)
    print(str(Freight_Car))
    station = Station.create_station(0, 0, 0)
    freight_car = FreightCar(0, station, 14000, 10, 5, 4, 1, 0.0)

    freight_car.containers.append(NormalContainer(0, 1000))
    freight_car.containers.append(NormalContainer(1, 2000))
    freight_car.containers.append(HeavyContainer(2, 1500))
    freight_car.containers.append(HeavyContainer(3, 2000))
    freight_car.containers.append(HeavyContainer(4, 2000))
    freight_car.containers.append(RefrigeratedContainer(5, 1000))
    freight_car.containers.append(RefrigeratedContainer(6, 2000))

    current_containers = freight_car.getCurrentContainers()

    for container in current_containers:
        print(container)
    total_weight = sum(container.weight for container in current_containers)

    print("Total weight of containers in freight car:", total_weight)

    # Test Case 5:
    print("Test case 5:")
    station = Station(0, "Station0",float())
    fc = FreightCar(1, station, 10000, 10, 5, 3, 4, 50.0)
    print(fc)

    # Test Case 6:
    print("Test Case 6:")

    def create_destination_station(create_freight_car):
        return Station(ID=1, X=10, Y=10)

    def create_freight_car(self):



        freight_car = FreightCar(ID=0, currentStation=Station(ID=0, X=0, Y=0), totalWeightCapacity=10000,
                          maxNumberOfAllContainers=10, maxNumberOfHeavyContainers=5,
                          maxNumberOfRefrigeratedContainers=2, maxNumberOfLiquidContainers=2,
                          double_fuelConsumptionPerKM=0.1)

        destination_station = Station(ID=1, X=10, Y=10)

        has_enough_fuel = freight_car.calculate_fuel_consumption(destination_station)

        print("[ Fuel Consumption : {0} ]".format(has_enough_fuel))

        distance_to_destination = freight_car.currentStation.getDistance(destination_station)

        freight_car.frightcar_to_station(destination_station)

        print(freight_car)
        print("Freight Reached Destination!")

        has_enough_fuel = freight_car.calculate_fuel_consumption(
            destination_station)
        print("[ Fuel Consumption : {0} ]".format(has_enough_fuel))


        return freight_car




    #Test Case 7:

    print("Test Case 7:")

    freight_car = FreightCar(ID=0, currentStation=Station(ID=0, X=0, Y=0), totalWeightCapacity=10000,
                             maxNumberOfAllContainers=10, maxNumberOfHeavyContainers=5,
                             maxNumberOfRefrigeratedContainers=2, maxNumberOfLiquidContainers=2,
                             double_fuelConsumptionPerKM=0.1)
    freight_car.add_fuel(30.20)
    print(f"[ Fuel Added : {0} ] ".format(freight_car.double_fuel))

# Run code:

if __name__ == '__main__':
    Main()
