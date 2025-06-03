# Use *args for any no.of positional arguments
def add(*args):
    print(sum(args))

# add(1,2,3,4,5,6,7,8,9,1)

# Use **kwargs for many keyword arguments
def calculate(**kwargs):
    print(kwargs["add"])
    print(kwargs["multiply"])

calculate(add=2, multiply=3)