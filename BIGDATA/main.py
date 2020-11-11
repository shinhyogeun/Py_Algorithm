# 카카오 인턴 대비 문자열 압축

def solution(s):
    # 가능한 경우 s의 길이
    a = len(s)//2
    front = 1
    result = ""
    for i in range(1,a+1):
        for j in range((len(s)//i)):
            if j != ((len(s)//i)-1):
                if s[j*i:(j+1)*i] == s[(j+1)*i:(j+2)*i]:
                    front += 1
                else:
                    if front != 1:
                        result += str(front) + s[j*i:(j+1)*i]
                        front = 1
                    else:
                        result += s[j*i:(j+1)*i]
            else:
                if front != 1:
                    result += str(front) + s[j*i:(j+1)*i]
                    front = 1
                else:
                    result += s[j*i:(j+1)*i]
        result += s[i*(len(s)//i):]
    print(result)

solution("asdasd")