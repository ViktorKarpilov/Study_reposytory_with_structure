import validation as val
"""СССССССССССС"""
def entering():
    """
    Does nothing more than demonstrate syntax.

    This is an example of how a Pythonic human-readable docstring can
    get parsed by doxypypy and marked up with Doxygen commands as a
    regular input filter to Doxygen.

    Args:
        arg1:   A positional argument.
        arg2:   Another positional argument.

    Kwargs:
        kwarg:  A keyword argument.

    Returns:
        A string holding the result.

    Raises:
        ZeroDivisionError, AssertionError, & ValueError.

    Examples:
        >>> myfunction(2, 3)
        '5 - 0, whatever.'
        >>> myfunction(5, 0, 'oops.')
        Traceback (most recent call last):
            ...
        ZeroDivisionError: integer division or modulo by zero
        >>> myfunction(4, 1, 'got it.')
        '5 - 4, got it.'
        >>> myfunction(23.5, 23, 'oh well.')
        Traceback (most recent call last):
            ...
        AssertionError
        >>> myfunction(5, 50, 'too big.')
        Traceback (most recent call last):
            ...
        ValueError
    """
    number = input("Enter number:")
    answer = input("Want to exit ?('yes',something else)")
    if(not val.int_valid(number)):
        print("Enter sommething that more 'intrative' =)")
        return entering()
    else:
        if(answer == "yes" or answer == "Yes"):
            return number
        return number+"/"+entering()
    return "0"
def bigger(numbers_set):
    """Take set and back bigger element in that set"""
    number = int(numbers_set.pop())
    second_number = False
    if(len(numbers_set)!=0):
        second_number = bigger(numbers_set)
    if(second_number and number<second_number):
        print(number<second_number)
        print(str(second_number)+"B")
        print(str(number)+"A")
        return second_number
    else:
        print(number)
        return number

numbers_string = entering()
numbers_set = set(numbers_string.split("/"))
print(bigger(numbers_set))


