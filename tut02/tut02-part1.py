def reduce_to_single_digit(n):
    n = abs(n)

    while n >= 10:
        digits = str(n)
        digit_sum = 0

        for digit in digits:
            digit_sum += int(digit)

        n = digit_sum
    return n

n = input("Enter a number : ")
n = int(n)
result = reduce_to_single_digit(n)
print(result)