question = [
    '   + -- + - + -   ',
    '   + --- + - +   ',
    '   + -- + - + -   ',
    '   + - + - + - +   ',
]
binaries = ["" for _ in range(len(question))]
chars = ['' for _ in range(len(question))]

for i in range(len(question)):
    # 공백 제거
    question[i] = question[i].replace(' ', '')
    # 이진수화
    for j in range(len(question[i])):
        if question[i][j] == '+':
            binaries[i] += '1'
        elif question[i][j] == '-':
            binaries[i] += '0'

# 십진수로 변환 후 아스키코드로 문자화
for i in range(len(binaries)):
    chars[i] = chr(int(binaries[i], 2))

print(''.join(chars))