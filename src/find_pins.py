from itertools import permutations

def find_4_digit_pins(numbers: list[int]) -> list[str]:
    
    # error handling
    if type(numbers) != type([]):
        raise TypeError('numbers must be a list of numbers')
    if len(numbers) > 4:
        raise ValueError('cannot have more than 4 numbers in a 4 digit pin')

    retList = []
    if len(numbers) == 4:
        for perm in permutations(numbers):

            retList.append(list(perm))
    elif len(numbers) == 1: #just 1 number lol
        retList = numbers * 4

    else:  # need to add more - recursive call w random one appended to list
        for num in numbers:
            curr_numbers = numbers.copy()
            curr_numbers.append(num)
            retList.extend(find_4_digit_pins(curr_numbers))
    return retList

            