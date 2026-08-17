# using numpy to implement a network
# the computer does not know what a sine wave is
# the dataset: i provide it with 2000 coordinate of x and y  the goal of the program is to learn a maths formula that matches these coordinates 

import numpy as np
import math

# rand i/o data
x = np.linspace(-math.pi, math.pi, 2000)
y = np.sin(x)

# randomly initialize weights
# set up a cubic equation y = a + bx + cx^2 + dx^3
# assigns random weights
a = np.random.randn()
b = np.random.randn()
c = np.random.randn()
d = np.random.randn()

lr= 1e-6
for t in range(2000):
    # Forward pass
    # use current weights to pred the y values 
    y_pred = a + b * x + c * x ** 2 + d * x ** 3


    # compute and output loss
    loss = np.square(y_pred - y).sum()
    if t % 100 == 99:
        print(t, loss)
    # note: back propagration is to answer
    """
    How much does the total loss change if i tweak a single weight
    """
    # Power Rule applied to Loss = (y_pred - y)^2
    # dLoss / dy_pred = 2 * (y_pred - y)
    grad_y_pred = 2.0 * (y_pred - y)

    # Chain Rule: dLoss/da = (dLoss/dy_pred) * (dy_pred/da), where dy_pred/da = 1
    grad_a = grad_y_pred.sum()

    # Chain Rule: dLoss/db = (dLoss/dy_pred) * (dy_pred/db), where dy_pred/db = x
    grad_b = (grad_y_pred * x).sum()

    # Chain Rule: dLoss/dc = (dLoss/dy_pred) * (dy_pred/dc), where dy_pred/dc = x^2
    grad_c = (grad_y_pred * x ** 2).sum()

    # Chain Rule: dLoss/dd = (dLoss/dy_pred) * (dy_pred/dd), where dy_pred/dd = x^3
    grad_d = (grad_y_pred * x ** 3).sum()
    
    # Note: .sum() aggregates the gradients across all 2000 data points.


    # update weights
    a -= lr * grad_a
    b -= lr * grad_b
    c -= lr * grad_c
    d -= lr * grad_d

print(f"Results: y= {a} + {b} x + {c} x^2 + {d} x^3 ")