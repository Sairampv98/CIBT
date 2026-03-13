if __name__ == '__main__':
        N = int(input())
        list_name = []
        list_score = []
        #nested_list = []
        for i in range(N):
            list_name.append(input())
            list_score.append(input())
        #nested_list = list_name + list_score
        convert = map(float,list_score)
        temp = list(convert)
        loweset_score = min(temp)
        number_of_lowest_pos = []
        loweset_removed = []
        final_name = []
        def number(n,lowest,test):
            num = []
            for i in range(n):
                if (lowest== test[i]):
                    num.append(i)
            return num
        def remove(pos,test):
            for i in range(len(pos)):
                if(len(pos) == 1):
                    test.pop(pos[i])
                else:    
                    test.pop(pos[len(pos)-i-1])
            return test
        number_of_lowest_pos = number(N,loweset_score,temp)
        loweset_removed = remove(number_of_lowest_pos,temp)
        second_loweset_score = min(loweset_removed)
        number_of_second_lowest_pos = []
        number_of_second_lowest_pos = number(len(loweset_removed),second_loweset_score,loweset_removed)
        #second_loweset_score = str(second_loweset_score)
        def final(n,second_lowest):
            temp_final = []
            for i in range(n):
                if (second_lowest == float(list_score[i])):
                    temp_final.append(list_name[i])
            return temp_final
        final_name = final(N,second_loweset_score)
        final_name.sort()
        for i in range(len(final_name)):
            string_print = final_name[i]
            print(string_print)
        #list_name_score_wrong = list_name + list_score
        #print("====name-score-wrong====")
        #print(list_name_score_wrong)
        #list_name_score = []
        #for i in range(N):
              #list_name_score.append(list_name[i])
              #list_name_score.append(list_score[i])
        #print("====name-score-correct====")
        #print(list_name_score)
        #number_student = len(list_name)
        #number_grades = len(list_score)