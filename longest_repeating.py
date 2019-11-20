import pdb
def long_repeating(input_string):
    string_dict = dict()
    tmp = input_string[0]
    longest = 0
    tmp_long = 1
    for char in input_string:
##        pdb.set_trace()
        if tmp == char:
            tmp_long += 1
        else:
            tmp = char
            if longest < tmp_long: longest = tmp_long
            tmp_long = 1
##        if char in string_dict:
##            string_dict[char] += 1
##        else:
##            string_dict[char] = 1
##    longest = 0
##    pdb.set_trace()
##    for di in string_dict:
##        if string_dict[di] > longest:
##            longest = string_dict[di]
            

    return longest
