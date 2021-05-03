def recursive_nth_fibo(number):
    if number <= 1:
        return number
    else:
        return recursive_nth_fibo(number - 1 ) + recursive_nth_fibo(number - 2)

def main():
    number = int(input("Zadaj cislo:"))
    n_th = recursive_nth_fibo(number)
    fib_seq = []
    for num in range(number + 1):
        fib_seq.append(recursive_nth_fibo(num))
    print(fib_seq)

if __name__ == '__main__':
    main()
