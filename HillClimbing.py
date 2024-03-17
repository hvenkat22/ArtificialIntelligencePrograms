import random
def hill_climbing(func,x_min,x_max,step_size=0.01,max_iter=1000):
  current_x = random.uniform(x_min,x_max)
  for _ in range(max_iter):
    gradient=(func(current_x+step_size)-func(current_x))/step_size
    new_x=current_x + step_size*gradient
    if func(new_x) > func(current_x):
      current_x = new_x
    else:
      break
  return current_x,func(current_x)

def function(x):
  return -4*(x**2) + 2*x + 3

x_min=-10
x_max=10
opt_x,opt_val=hill_climbing(function,x_min,x_max)
print("Optimum x: %.2f"%opt_x)
print("Optimum value: %.2f"%opt_val)