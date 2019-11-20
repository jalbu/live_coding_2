def long_repeating(input_string):
    string_dict = dict()
    tmp = ''
    longest = 0
    tmp_long = 0
    for num, char in enumerate(input_string):
        if tmp == char:
            tmp_long += 1
        else:
            tmp = char
            if longest <= tmp_long:
                longest = tmp_long
            tmp_long = 1
            
    if longest <= tmp_long:
        longest = tmp_long
    return longest
