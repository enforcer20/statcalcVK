import unittest
#from Calculator.Calculator import Calculator
from Calculator import Calculator
#from CsvReader.CsvReader import CsvReader
import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_mean_calculator(self):
        ##test_data = CsvReader('/Tests/Data/Addition.csv').data
        ##for row in test_data:
        data = [1,2,3,4,5]
        self.assertEqual(self.calculator.popmean(data), 3)

    def test_sd_calculator(self):
        data = [1, 2, 3, 4, 5]
        self.assertEqual(self.calculator.stdev(data), 1.5811388300841898)


if __name__ == '__main__':
    unittest.main()

