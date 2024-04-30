import numpy

from readers import csv_reader
from linear_models.models import SimpleLinearModel
from linear_models.training_methods import simple_gradient_descent
import numpy as np

if __name__ == '__main__':
    data = csv_reader.read_csv("data/kc_house_data.csv")
    #data_cut = csv_reader.read_batch_csv(2, 4, "data/kc_house_data.csv")
    data = numpy.array(data)
    price= data[:, 2].astype('float64')
    max_price = np.max(price)
    #print(price)
    price = price/ max_price
    size = data[:, 5].astype('float64')
    max_size = np.max(size)
    size = size / max_size
    #print(price)
    theta, b = simple_gradient_descent.gradient_descent(size, price, 2, 1, 10000, 0.001)
    print(theta)
    print(b)