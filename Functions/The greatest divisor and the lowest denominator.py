def divisors(num):
    s = []
    for i in range(1, num + 1):
        if num % i == 0:
            s.append(i)
        else:
            continue
    return s

def gcd_and_lcd(num1, num2):
    
    # to find divisors and convert to set
    s_num1 = set(divisors(num1)) 
    s_num2 = set(divisors(num2))
    
    # finding gcd and lcd
    gcd = max(s_num1 & s_num2)
    lcd = (num1 * num2) / gcd
    
    print("The greatest common divisor is", gcd)
    print("The lowest common denominator is", lcd)
    print('Divisors of ', num1, ' and ', num2, 'is')
    print(divisors(num1), '\n and \n', divisors(num2) )
    
    return None
    
