
def check_if_match(single_str) -> str:
    working_stack = []  # 用栈来辅助，元素类型为(index, char)
    result_str = [' '] * len(single_str)  # 结果字符串数组，如果不考虑顺序只是发出？和x的相对顺序，则不需要该数组，空间复杂度能降到O(1)
    for i in range(len(single_str)):
        if single_str[i] == '(':
            working_stack.append((i, single_str[i]))
        elif single_str[i] == ')':
            if len(working_stack) > 0 and working_stack[-1][1] == '(':
                working_stack.pop()
            else:
                result_str[i] = '?'
        else:
            continue

    while len(working_stack) > 0:
        term = working_stack.pop()
        result_str[term[0]] = 'x'

    return ''.join(result_str)

if __name__ == '__main__':
    print('please input the string(默认换行即enter为字符串结束): ')
    while True:
        sentence = input()
        if input == 'stop':
            print('program stops!')
            break
        else:
            print(check_if_match(sentence))
        print('once more:')

