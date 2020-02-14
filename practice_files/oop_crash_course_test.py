import unittest
from oop_crash_course_car import Tesla
from oop_crash_course_instantiation import generate_teslas


class TestCar(unittest.TestCase):

    def test_default_driverless(self):
        a_tesla = Tesla(4, 'Model S')
        self.assertEqual(a_tesla.driverless_enabled, False)


class TestProduction(unittest.TestCase):

    def test_legal_model_name(self):
        teslas = generate_teslas(10)
        models = ['Model 3', 'Model S', 'Model X']

        for tesla in teslas:
            self.assertIn(tesla.model, models)


if __name__ == '__main__':
    unittest.main()
