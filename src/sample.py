def sample_function() -> None:
    print("Hello from the sample function!")


def get_addition(x: float, y: float) -> float:
    return x + y


# Adding type hints to bits and pieces is helpful but not necessary
def get_subtraction(x, y):
    return x - y


def get_multiplication(x: float, y: float) -> float:
    """
        Triple quote docstrings are also sometimes helpful for documenting
        what functions want to do.

        x: floating point number
        y: floating point number

        returns x times y
    """
    return x * y


def get_division(x: float, y: float) -> float:
    assert(y != 0) # you can add assertions to enforce certain things to be true
    
    divisor_is_zero: bool = y == 0
    assert(not divisor_is_zero) # you can also pass any boolean value into assert

    return x / y



class TestClass:

    value: str = "" # Attributes can either be declared here

    def __init__(self) -> None:
        self.another: int = 0 # or dynamically inside of class methods

        # variable declartions that omit `.self` are NOT kept alive once the function ends (is popped off the stack)
        summation = get_addition(45, 24)

    
    def function1(self) -> None:
        print(self.another) # when you pass `self` into a function you can reference other class attributes

    
    def function2() -> None:
        print(f"The 'f' before the quotation marks allowes us to embed values directly into the string like this: {get_multiplication(45, 24)}")


    def function3() -> None:
        try:
            self.function1()
        except NameError as e:
            print(
                f"Program ecountered an error `{type(e)}: {e}`! But, we are choosing to handle it 'gracefully' instead of crashing"
            )