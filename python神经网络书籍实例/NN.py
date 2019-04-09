# neural network class definition
import numpy as np
from scipy import special
class neuralNetwork:

    # initialise the neural network
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        # set number of nodes in each input,hidden,output layer
        self.indoes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        # link weight matrices,wih and who
        # wgight inside the arrays are w_i_j, where link is from node i to node j in the next layer
        self.wih = np.random.normal(0.0, pow(self.hnodes, -0, 5), (self.hnodes, self.indoes))
        self.who = np.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))
        # learning rate
        self.lr = learningrate

        #activation function is the sigmod function
        self.activation_function = lambda x: special.expit(x)
    # train the neural Network
    def train(self, inputs_list, targets_list):
        inputs = np.array(inputs_list, ndmin=2).T
        targets = np.array(targets_list, ndmin=2).T

        hidden_inputs=np.dot(self.wih,inputs)
        hidden_outputs = self.activation_function(hidden_inputs)
        final_inputs = np.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)
        
        output_errors = targets - final_outputs
        hidden_errors = np.dot(self.who.T, output_errors)
        self.who += self.lr * np.dot((output_errors * final_outputs * (1.0 - final_outputs)), np.transpose(hidden_outputs))
        self.wih+=self.lr*np.dot((hidden_errors*hidden_outputs*(1.0-hidden_outputs)),np.transpose(inputs))

    def query(self, inputs_list):
        # convert inputs list to 2d array
        inputs = np.array(inputs_list, ndmin=2).T
        #calculate signals into hidden layer
        hidden_inputs = np.dot(self.wih, inputs)
        hidden_oitputs = self.activation_function(hidden_inputs)
        final_inputs = np.dot(self.who, hidden_oitputs)
        final_outputs = self.activation_function(final_inputs)
        res=final_outputs.tolist()
        return res.index(max(res))