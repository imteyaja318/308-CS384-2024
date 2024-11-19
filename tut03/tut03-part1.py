import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2,int(math.sqrt(n)) + 1):
        if n%i == 0:
            return False
    return True




num = input("Enter a number: ")
a = []
num_list = list(num)

for i in range(len(num_list)):
    for j in range(len(num_list)):
        temp = num_list[:]
        temp[i] , temp[j] = temp[j] , temp[i]
        permutn = int(''.join(temp))
        if permutn not in a:
            a.append(permutn)
print(a)
for number in a:
    if is_prime(number):
        print("rotational prime :",number)