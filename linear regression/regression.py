"""  @author Victor I. Afolabi  A.I. Engineer & Software developer  javafolabi@gmail.com  Created on 25 August, 2017 @ 8:15 PM.  Copyright (c) 2017. victor. All rights reserved."""import numpy as npclass LinearRegression(object):    def __init__(self, learning_rate=1e-4):        self.m = 0        self.b = 0        self.learning_rate = learning_rate    def fit(self, data, num_iter=1000):        for _ in range(num_iter):            self.__gradient_descent(data)        return self.m, self.b    def __gradient_descent(self, data):        n = len(data)        m_gradient = 0        b_gradient = 0        for _, d in enumerate(data):            x = d[0]            y = d[1]            m_gradient += (2 / n) * -x * (y - ((self.m * x) + self.b))            b_gradient += (2 / n) * -(y - ((self.m * x) + self.b))        self.m = self.m - (self.learning_rate * m_gradient)        self.b = self.b - (self.learning_rate * b_gradient)if __name__ == '__main__':    clf = LinearRegression(learning_rate=1e-5)    data = np.genfromtxt('data.csv', delimiter=',')    clf.train(data)    print('m = {:.2f} b = {:.2f}'.format(clf.m, clf.b))