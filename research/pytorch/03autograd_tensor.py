# numpy is an amazing tool but it cannot utilize Gpus to accelerate 
import numpy as np
import math
import torch

dtype = torch.float
device = torch.accelerator.current_accelerator().type() if torch.accelerator.is_available() else "cpu"
print(f"using {device} device")
torch.set_default_device(device)

# create tensors to hold input and outputs. 
# by default when creating tensors ...torch keeps require_grad = False
# compute gradient with respect to this tensors
x = torch.linspace(-1, 1, 2000, dtype=dtype) 
y = torch.exp(x) # A Taylor expansion would be 1 + x + (1/2) x**2 + (1/3!) x**3 + ...

# Randomly initialize weights
a = torch.randn((), device=device, dtype=dtype)
b = torch.randn((), device=device, dtype=dtype)
c = torch.randn((), device=device, dtype=dtype)
d = torch.randn((), device=device, dtype=dtype)

learning_rate = 1e-6
for t in range(2000):
    # Forward pass
    y_pred = a + b * x + c * x ** 2 + d * x ** 3

    # Compute and print loss
    loss = np.square(y_pred - y).sum()
    if t % 100 == 99:
        print(t, loss)

    # Backprop to compute gradients of a, b, c, d with respect to loss
    grad_y_pred = 2.0 * (y_pred - y)
    grad_a = grad_y_pred.sum()
    grad_b = (grad_y_pred * x).sum()
    grad_c = (grad_y_pred * x ** 2).sum()
    grad_d = (grad_y_pred * x ** 3).sum()

    # Update weights
    a -= learning_rate * grad_a
    b -= learning_rate * grad_b
    c -= learning_rate * grad_c
    d -= learning_rate * grad_d

print(f'Result: y = {a} + {b} x + {c} x^2 + {d} x^3')