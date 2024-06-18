def minion_game(string):
    # your code goes here
    p1 = 0
    p2 = 0
    vowels = ('A', 'E', 'I', 'O', 'U')
    str_len = len(string)
    for i in range(str_len):
        if string[i] not in vowels:
            p1 += str_len - i
        else:
            p2 += str_len - i
    if p1 > p2:
        print('Stuart', p1)
    elif p1 < p2:
        print('Kevin', p2)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)
