if __name__ == '__main__':
    a = int(input())
    b = int(input())

    if(1<=a) and (a<=10**10) and (1<=b) and (b<=10**10):
        print(a+b)
        print(a-b)
        print(a*b)
    else:
        print("Numbers a and b should be between 1-10^10")
