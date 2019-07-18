def reverse_str(s):
    str_list = list(s)
    length = len(str_list)
    reverse_str_part(str_list,0,length-1)
    i = 0
    print(str_list)
    while i < length:
        if str_list[i] != '':
            start = i
            end = i + 1
            while end < length and str_list[end] != ' ':
                end += 1
            reverse_str_part(str_list, start, end)
            i = end + 1
        else:
            i += 1
    print(''.join(str_list))

def reverse_str_part(s, start, end):
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1


a = 'student. a am I'
reverse_str(a)
