def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

my_list = [1, 2, 3, 4, 5]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

#Alternative solution using exception handling:

def calculate_average_exception(numbers):
    try:
        return sum(numbers) / len(numbers)
    except ZeroDivisionError:
        return 0

my_list = [1, 2, 3, 4, 5]
average = calculate_average_exception(my_list)
print(f"The average (exception handling) is: {average}")

my_empty_list = []
average_empty = calculate_average_exception(my_empty_list)
print(f"The average of an empty list (exception handling) is: {average_empty}")
