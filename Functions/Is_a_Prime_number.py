def is_prime(num):
    check = []
    if num == 0 or num == 1:
        return False
    for i in range(2, num + 1):
        if num % i == 0:
            check.append(True)
    if len(check) == 1:
        return True
    else:
        return False
