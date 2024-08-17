def is_prime(func):
    def PrimeCheck(*args, **kwargs):
        result = func(*args, **kwargs)
        if result <= 1:
            print('составное')
        else:
            for i in range(2, int(result/2 + 1)):
                if result % i == 0:
                    print("составное")
                    break
            else:
                print('простое')
        return result
    return PrimeCheck
@is_prime
def sum_three(a,b,c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)

