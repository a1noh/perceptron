import random
class perceptron(object):
    weights = []
    lc = 0
    def __init__(self,n, lc):
        for i in range(n):
            self.weights.append(random.choice([-1,1])) #add random weights
        self.c = lc
 
#    def train(inputs, desired):
#        guess = 
    def train(self, inputs, desired):
        guess = perceptron.feedforward(self,inputs)
        error = desired - guess
        for i in range(len(self.weights)):
            self.weights[i] += self.lc * error * guess 

    def feedforward(self,inputs):#checked this worked
        sum = 0
        for i in range(len(self.weights)):
            sum += inputs[i] * self.weights[i]
        return self.activate(sum)

    def activate(self,sum):
        if (sum > 0):
            return 1
        else:
            return -1

weights = perceptron(3,0.1) # how to make perceptron (n,0.1)
print(perceptron.feedforward(weights,[2,1,3])) #this is how you use methods in class