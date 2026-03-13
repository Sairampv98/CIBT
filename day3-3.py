# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
N = int(input())
l = map(int,input().split())
t = tuple(l)
h = hash(t)
if(len(t)==n):
    print(h)
else:
    print(f"inputted value greater than {N}")
'''
'''
if __name__ == '__main__':
    n = int(input())
    t = map(int, input().split())
    print(hash(tuple(t)))

'''

# Source - https://stackoverflow.com/a/79353152
# Posted by Ashok Kumar
# Retrieved 2026-03-11, License - CC BY-SA 4.0
'''
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))
'''


N = int(input())
l = map(int,input().split())
t = tuple(l)
h = hash(t)
if(len(t)==N):
    print(h)
else:
    print(f"inputted value greater than {N}")
