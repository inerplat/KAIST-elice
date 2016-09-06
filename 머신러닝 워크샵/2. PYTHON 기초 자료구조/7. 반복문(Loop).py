def exercise(big_list):
    # 1
    small_list = []
    # 2

    for i in range(0,len(big_list)):
        small_list.append(big_list[i].lower())
    return small_list

print(exercise(['C#', 'JAVASCRIPT', 'JAVA', 'PYTHON', 'MATLAB', 'R']))
