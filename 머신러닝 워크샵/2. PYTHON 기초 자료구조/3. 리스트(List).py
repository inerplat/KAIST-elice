def exercise(my_language):
    # 1
    programming_languages = ["C#","Javascript","Java","Python","Matlab","R"]

    # 2
    del programming_languages[1]
    # 3
    programming_languages.append('C++')
    # 4
    is_my_language=my_language in programming_languages
    return is_my_language

print(exercise('R'))
