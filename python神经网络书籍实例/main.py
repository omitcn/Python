from NN import neuralNetwork
import numpy as np
import matplotlib.pyplot as plot
import scipy.misc

n = neuralNetwork(784, 100, 10, 0.2)
data_file = open('train.csv', 'r')
data_list = data_file.readlines()
data_file.close()
for record in data_list:
    all_values = record.split(',')
    inputs = (np.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
    targets = np.zeros(10) + 0.01
    targets[int(all_values[0])] = 0.99
    n.train(inputs, targets)
'''
test_file = open('test.csv', 'r')
test_list = test_file.readlines()
test_file.close()
all_value = test_list[9].split(',')
print(all_value[0], type(all_value[0]))
image_array = np.asfarray(all_value[1:]).reshape((28, 28))
plot.imshow(image_array, cmap='Greys', interpolation='None')

print(n.query((np.asfarray(all_value[1:]) / 255.0 * 0.99) + 0.01))
'''
img_array = scipy.misc.imread('9.png', flatten=True)
img_data = 255.0 - img_array.reshape(784)
img_data = (img_data / 255.0 * 0.99) + 0.01
print(n.query(np.asanyarray(img_data)))
