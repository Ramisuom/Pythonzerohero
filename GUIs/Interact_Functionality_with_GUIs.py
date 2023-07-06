# Start with some imports!

from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets

# Very basic function
def func(x):
    return x

# Generate a slider to interact with
interact(func, x=10,);

# Booleans generate check-boxes
interact(func, x=True);

# Strings generate text areas
interact(func, x='Hi there!');

# Using a decorator!
@interact(x=True, y=1.0)
def g(x, y):
    return (x, y)

interact(func, x=1);