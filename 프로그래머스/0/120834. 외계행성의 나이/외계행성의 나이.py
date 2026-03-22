def solution(age):
    answer = []
    a = str(age)
    list_answer = list(a)
    
    for i in list_answer:
        if i == "0":
            answer.append("a")
        elif i == "1":
            answer.append("b")
        elif i == "2":
            answer.append("c")
        elif i == "3":
            answer.append("d")
        elif i == "4":
            answer.append("e")
        elif i == "5":
            answer.append("f")
        elif i == "6":
            answer.append("g")
        elif i == "7":
            answer.append("h")
        elif i == "8":
            answer.append("i")
        elif i == "9":
            answer.append("j")
            
    answer = "".join(answer)

    return answer