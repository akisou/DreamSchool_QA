def duplication_decline(working_str):
    working_str = list(working_str)
    char2num = dict()

    # 记录次数
    for i in range(len(working_str)):
        if working_str[i] in char2num.keys():
            char2num[working_str[i]] += 1
            working_str[i] = '-'
        else:
            char2num[working_str[i]] = 1

    return ''.join(working_str)


if __name__ == '__main__':
    print('please input the string(默认换行即enter为字符串结束): ')
    while True:
        sentence = input()
        if input == 'stop':
            print('program stops!')
            break
        else:
            print(duplication_decline(sentence))
        print('once more:')
