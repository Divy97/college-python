# .Write a Pytthon program that will find power of any number.

base = 3
exponent = 2

result = pow(base, exponent)


def power(base, exponent):
    result = 1
    for exponent in range(exponent, 0, -1):
        result = result * base
    return result


print("Answer is =", power(2, 4))
print("Answer = " + str(result))
