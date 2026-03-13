if __name__ == '__main__':
    N = int(input()) 
    a = [] 
    #arr = (input().split())
    #user_input = list(arr)
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
                list_output.append(temp_value)
            if(list_input[i]=='sort'):
                list_output = a
                list_output.sort()
            if(list_input[i]=='reverse'):
                list_output = a
                list_output.reverse()
            if(list_input[i]=='pop'):
                list_output = a
                list_output.pop()
            if(list_input[i]=='print'):
                list_output = a
                print(list_output)
        return list_output

    for i in range(N): 
        '''if(i==0):
            
            a = parse_list(user_input,a)
        '''
        if(i!=N):
            arr = (input().split())
            user_input = list(arr)
            a = parse_list(user_input,a)
        

