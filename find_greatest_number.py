

def find_greatest(numbers) -> tuple:
    """
    accepts list of numbers
    return greatest number
    """
    greatest = max(numbers)
    return greatest


# numbers should be separated by commas
numbers = input("Enter numbers separated by commas: ").split(",")
print(find_greatest(numbers))