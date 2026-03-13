
#def replace(int):
#    return int

#squared = list(map(replace, input.split()))
#print(squared)

#a,b = map(int, input().split())
#print(a+b)
'''
name = input()
age = int(input())
cgpa = input()
grade = input()
decimal_places = 0
for i in range (len(cgpa)):
    if(cgpa[i] == '.'):
        decimal_places = i+3
corrected_cgpa = cgpa[0:decimal_places]
float_cgpa = float(corrected_cgpa)
print("Name:",name)
print("Age:",age)
print("CGPA:", float_cgpa)  
print("Grade:",grade)
'''
'''
arr = (input().split())
user_input = list(arr)
a = [9,5,6,1]
#print(a)
def parse_list(list_input,a):
        list_output = []
        for i in range(len(list_input)):
            if(list_input[i]=='insert'):
                temp_pos = int(list_input[i+1])
                temp_value = int(list_input[i+2])
                list_output = a
                list_output.insert(temp_pos, temp_value)
            if(list_input[i]=='remove'):
                temp_value = int(list_input[i+1])
                list_output = a
                list_output.remove(temp_value)
            if(list_input[i]=='append'):
                temp_value = int(list_input[i+1])
                list_output = a
                list_output.remove(temp_value)
            if(list_input[i]=='sort'):
                list_output = a
                list_output.sort()
            if(list_input[i]=='reverse'):
                list_output = a
                list_output.reverse()
            if(list_input[i]=='print'):
                list_output = a
                print(list_output)
        return list_output

output = parse_list(user_input,a)
'''
'''
arr = input().split()
a = list(arr)
print(a)
'''
'''
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
'''

#a = [1,2]
#a.pop(0)
#print(a)


'''
arr = list(map(int, input().split()))
height_set = set(arr)
height_added = sum(height_set)
number_of_heights = len(height_set)
average = height_added/number_of_heights
print(arr)
print(height_set)
print(height_added)
print(number_of_heights)
print(f"{average:.3f}")
'''
'''
size_of_list = int(input())
empty = [input() for i in range(size_of_list)]
empty_lis = []
for i in range(size_of_list):
    empty_lis.append(input())

print(empty)
print(empty_lis)
'''
'''
input_string = input()
str_arr = input_string.split()
convert = map(int, str_arr)
arr = list(convert)
height_set = set(arr)
print(arr)
print(height_set)
'''


'''
myset = {1, 2}
myset = set(['a', 'b'])
print(myset)
myset.add('c')
print(myset)
myset.add('a')
print(myset)
myset.add((5, 4))
print(myset)
myset.update([1, 2, 3, 4])
print(myset)
myset.update({1, 7, 8})
print(myset)
myset.update({1, 6}, [5, 13])
print(myset)
myset.discard(13)
print(myset)
myset.remove(10)
print(myset)
'''

'''
a = {2, 4, 5, 9}
b = {2, 4, 11, 12}
print("Input a", a)
print("Input b", b)
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))
'''

def greet():
    pass
    
print(3.50 + 1)