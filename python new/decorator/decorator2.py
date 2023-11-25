def decorator(func):  # Define a decorator function that takes another function as an argument
    def wrapper():     # Define a wrapper function to modify the behavior of the original function
        print("Decorating before the original function")
        func()         # Call the original function
        print("Decorating after the original function")
    return wrapper     # Return the wrapper function

@decorator            # Use the @ syntax to apply the decorator to the hello function
def hello():
    print("Hello")

  # Call the decorated hello function
hello()
