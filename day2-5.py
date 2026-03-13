if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    A = list(arr)
    print(A)
    B = [input() for i in range(n)]
    print(B)
    if(len(A)==n):
        maximum = max(A)
        while (max(A) == maximum):
            A.remove(maximum)
        runnerUp = max(A)
        print(runnerUp)
    else:
        print(f"input number larger than {n}")