def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        ans = bin(arr1[i]|arr2[i])[2:]
        ans = ans.rjust(n,'0')
        text = ''
        print(ans)
        for j in ans:
            if j == '1':
                text += '#'
            if j == '0':
                text += ' '
        answer.append(text)
    return answer