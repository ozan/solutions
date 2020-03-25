def is_armstrong_number(number):
    digits = str(number)
    return number == sum(int(d)**len(digits) for d in digits)
