def average(array):
    # your code goes here
    height_set = set(arr)
    height_added = sum(height_set)
    number_of_heights = len(height_set)
    average = f"{height_added/number_of_heights:.3f}"
    
    return average

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)