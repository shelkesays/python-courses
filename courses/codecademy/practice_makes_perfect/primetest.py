def is_prime(number):
    if number > 2:
        for num in range(2, number):
            if number % num == 0:
                return False
        else:
            return True
    else:
        if number == 2:
            return True


print is_prime(4437843)
