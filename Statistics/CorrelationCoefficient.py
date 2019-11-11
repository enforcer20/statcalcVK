from Statistics.PopulationMean import mean
from Statistics.StandardDeviation import st_dev
from Calculator.Multiplication import multiplication
from Calculator.Subtraction import subtraction
from Calculator.Division import division
from Statistics.SampleGenerator import getSample
from CsvReader.CsvReader import CsvReader
#import numpy


def Pop_correlation_coefficient(x_data,y_data):


    x_mean = mean(x_data)
    y_mean = mean(y_data)
    a = []
    b = []
    ab = []
    tot_sum = 0
    x = st_dev(x_data)
    y = st_dev(y_data)
    divisor = multiplication(x, y)
    #z = len(x_data)

    for i in x_data:
        new1 = subtraction(x_mean, i)
        zx = division(new1, x)
        a.append(zx)

    for i in y_data:
        new2 = subtraction(y_mean, i)
        zy = division(new2, y)
        b.append(zy)

    for i in range(len(x_data)):
        ab = a[i] * b[i]
        tot_sum = tot_sum + ab

    cal_result = tot_sum / 4

    return cal_result

# covriance = cov(X, Y) = (sum (x - mean(X)) * (y - mean(Y)) ) * 1/(n-1)
# covariance(X, Y) / (stdv(X) * stdv(Y))
