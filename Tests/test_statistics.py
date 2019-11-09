import unittest
from Statistics.Statistics import Statistics
from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics('Tests/Data/UnitTestStats.csv')

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_decorator_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)


    def test_Population_Mean_calculator(self):
        test_data = CsvReader('Tests/Data/StatCalcData.csv').data
        answer = CsvReader('Tests/Data/UnitTestStatsAnswers.csv').data
        lst = []
        for row in test_data:
            y = int(row['Value 1'])
            lst.append(y)
        # for column in answer:
        # result = float((column['mean']))
        self.assertEqual(self.statistics.newmean(lst), 72.94494494494495)


    def test_Sample_Mean_calculator(self):
        test_data = CsvReader('Tests/Data/StatCalcData.csv').data
        lst = []
        for row in test_data:
            y = int(row['Value 1'])
            lst.append(y)
        x, z = self.statistics.sammean(lst)

        self.assertEqual(x, z)

    def test_median_calculator(self):
        ##test_data = CsvReader('/Tests/Data/Addition.csv').data
        ##for row in test_data:
        data = [1, 2, 3, 4, 5, 6]
        self.assertEqual(self.statistics.med(data), 3.5)

    def test_mode_calculator(self):
        ##test_data = CsvReader('/Tests/Data/Addition.csv').data
        ##for row in test_data:
        data = [1, 2, 3, 4, 5, 6, 3]
        self.assertEqual(self.statistics.mod(data), 3)

    def test_Standard_Deviation_calculator(self):
        data = [1, 2, 3, 4, 5]
        self.assertEqual(self.statistics.stddev(data), 1.5811388300841898)

    def test_Sample_Standard_Deviation_calculator(self):

        test_data = CsvReader('Tests/Data/StatCalcData.csv').data
        lst = []
        for row in test_data:
            y = int(row['Value 1'])
            lst.append(y)
        x, z = self.statistics.sampstdev(lst)
        x = round(x, 3)
        z = round(z, 3)

        self.assertEqual(x, z)

    def test_confidence_interval_calculator(self):
        data = [1, 2, 3, 4, 5]
        conf = 95
        self.assertEqual(self.statistics.confintv(data, conf), (4.39, 1.61))

    def test_zscore_calculator(self):
        data = [1, 2, 3, 4, 5]
        x = round(-1.2649110640673518, 7)
        self.assertEqual(self.statistics.z_score(data), x)

    def test_population_variance_calculator(self):
        data = [1, 2, 3, 4, 5]
        self.assertEqual(self.statistics.pvariance(data), 2.5000000000000004)

    def test_proportion_calculator(self):
        data = [1, 2, 3, 4, 5, 6]
        self.assertEqual(self.statistics.med(data), 3.5)


if __name__ == '__main__':
    unittest.main()
