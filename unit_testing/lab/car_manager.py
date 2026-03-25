class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


from unittest import TestCase, main



class TestCar(TestCase):
    def setUp(self):
        self.car = Car("BMW", "X5", 10, 60)

    def test_car_is_initialized_correctly(self):
        self.assertEqual("BMW", self.car.make)
        self.assertEqual("X5", self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(60, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_should_raise_when_empty(self):
        with self.assertRaises(Exception) as ex:
            Car("", "X5", 10, 60)
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_should_raise_when_empty(self):
        with self.assertRaises(Exception) as ex:
            Car("BMW", "", 10, 60)
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_should_raise_when_zero(self):
        with self.assertRaises(Exception) as ex:
            Car("BMW", "X5", 0, 60)
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_consumption_should_raise_when_negative(self):
        with self.assertRaises(Exception) as ex:
            Car("BMW", "X5", -1, 60)
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_should_raise_when_zero(self):
        with self.assertRaises(Exception) as ex:
            Car("BMW", "X5", 10, 0)
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_should_raise_when_negative(self):
        with self.assertRaises(Exception) as ex:
            Car("BMW", "X5", 10, -1)
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_should_raise_when_negative(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_should_raise_when_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_should_raise_when_negative(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-10)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_should_increase_fuel_amount(self):
        self.car.refuel(20)
        self.assertEqual(20, self.car.fuel_amount)

    def test_refuel_should_not_exceed_capacity(self):
        self.car.refuel(100)
        self.assertEqual(60, self.car.fuel_amount)

    def test_drive_should_raise_when_not_enough_fuel(self):
        self.car.fuel_amount = 5
        with self.assertRaises(Exception) as ex:
            self.car.drive(100)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_should_reduce_fuel_amount_when_enough_fuel(self):
        self.car.fuel_amount = 20
        self.car.drive(100)
        self.assertEqual(10, self.car.fuel_amount)


if __name__ == "__main__":
    main()
