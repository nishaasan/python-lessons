def multiplier_decorator(func):
    def wrapper(a, b):
        result = func(a, b)
        print(f"The result of multiplication is: {result}")
        return result

    return wrapper

@multiplier_decorator
def mul(a, b):
    return a * b

# Example usage:
result = mul(2, 3)
