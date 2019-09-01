import random
def sign(n):
    if n > 0:
        return 1
    else:
        return -1

class perceptron(object):
    weights = []
    lr = 0.001
    def __init__ (self):
        self.weights = []
        self.weights.append(random.choice([-1,1])) 
        self.weights.append(random.choice([-1,1])) 
    def guess(self, inputs):
        sum = 0
        for i in range(2):
            sum += inputs[i] * self.weights[i] #if weight is 0 don't change
        output = sign(sum)
        return output
    def train(self, inputs, target):
        guess = self.guess(inputs)
        error = target - guess
        #tune all the weights
        for i in range(2):
            self.weights[i] += error * inputs[i] * self.lr #tweak it a little
    
#weights = perceptron()
#print(weights.weights[0])
#print(sign(2))