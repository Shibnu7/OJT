print("Enter a number")
x = int(input())

def calc_prime(num):
    if num <= 1:
        print(f"{num} is not a prime")
        return False
    else:
        for i in range(2, num//2 + 1):
            if num % i == 0:
                print(f"{num} is not a prime")
                return False
        print(f"{num} is a prime")
        return True

calc_prime(x)