#https://programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    answer = []
    new_id = new_id.lower()
    for x in new_id:
        if x.isalpha() or x.isalnum() or x == "-" or x == "_" or x == ".":
            answer.append(x)
    try:
        while True:
            check = False  
            if answer[0] == ".":
                answer =answer[1:]
                check = True
            if answer[-1] == ".":
                answer = answer[:-1]
                check = True
            for x in range(len(answer)-1):
                if answer[x] == "." and answer[x+1] == ".":
                    answer = answer[:x]+answer[x+1:]
                    check = True
                    break
            if check == False:
                break

    except:
        pass

    if len(answer) == 0:
        answer = "a"

    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == ".":
            answer= answer[:-1]
    if len(answer) <3:
        answer += answer[-1]*(3-len(answer))

    answer = "".join(answer)

    return answer