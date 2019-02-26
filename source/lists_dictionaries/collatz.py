def collatz(n):
    if n % 2 == 0:
        print(n // 2)
        return n // 2
    elif n % 2 == 1:
        print(3 * n + 1)
        return 3 * n + 1

def main():
    try:
        user = int(input('Give me integer:  '))
    except ValueError:
        print('I need integer value!')
        return None
    while user != 1: #infitity loop
        user = collatz(user)
        if user == 1:
            break
main()