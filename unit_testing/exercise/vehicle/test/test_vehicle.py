from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    fuel = 20.5
    horse_power = 135.5

    def setUp(self):
        self.vehicle = Vehicle(self.fuel, self.horse_power)

    def test_class_attributes_types(self):
        self.assertTrue(isinstance(self.vehicle.DEFAULT_FUEL_CONSUMPTION, float))
        self.assertTrue(isinstance(self.vehicle.fuel_consumption, float))
        self.assertTrue(isinstance(self.vehicle.fuel, float))
        self.assertTrue(isinstance(self.vehicle.capacity, float))
        self.assertTrue(isinstance(self.vehicle.horse_power, float))

    def test_init(self):
        self.assertEqual(self.fuel, self.vehicle.fuel)
        self.assertEqual(self.fuel, self.vehicle.capacity)
        self.assertEqual(self.horse_power, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_success(self):
        self.vehicle.drive(10)
        self.assertEqual(8, self.vehicle.fuel)

    def test_drive_fail(self):
        with self.assertRaises(Exception) as e:
            self.vehicle.drive(100)
        self.assertEqual("Not enough fuel", str(e.exception))

    def test_refuel_success(self):
        self.vehicle.fuel = 1
        self.vehicle.refuel(2.5)
        self.assertEqual(3.5, self.vehicle.fuel)

    def test_refuel_fail_to_much_fuel(self):
        self.vehicle.fuel = 15
        with self.assertRaises(Exception) as e:
            self.vehicle.refuel(20.5)
        self.assertEqual("Too much fuel", str(e.exception))

    def test_string(self):
        result = (f"The vehicle has {self.horse_power} "
                  f"horse power with {self.fuel} fuel left "
                  f"and 1.25 fuel consumption")
        self.assertEqual(result, str(self.vehicle))




if __name__ == '__main__':
    main()