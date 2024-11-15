from src.sample import TestClass



def main():
    test_class_instance = TestClass() # Constructs an instance of the class defined inside of `src/sample.py`
    
    test_class_instance.function1() # Calls a function that references the instance (passes `self` as a parameter implicitly)
    
    # You can also call functions that belong to the class itself and NOT instances
    TestClass.function2()

    TestClass.function3()


# This `if` statement ensures that the main function only runs if this file is run as the
# entry point
if __name__ == "__main__":
    main()