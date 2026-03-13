size_of_set_m = int(input())
set_m = set(map(int,input().split()))
size_of_set_n = int(input())
set_n = set(map(int,input().split()))

sym_diff = list(set_n.symmetric_difference(set_m))
sym_diff.sort()
for i in range(len(sym_diff)):
    string_print = sym_diff[i]
    print(string_print)
