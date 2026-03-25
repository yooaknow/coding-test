def solution(polynomial):
    terms = polynomial.split(" + ")
    
    x_sum = 0
    num_sum = 0
    
    for t in terms:
        if "x" in t:
            if t == "x":
                x_sum += 1
            else:
                x_sum += int(t.replace("x", ""))
        else:
            num_sum += int(t)

    result = ""
    
    if x_sum > 0:
        if x_sum == 1:
            result += "x"
        else:
            result += str(x_sum) + "x"
    
    if num_sum > 0:
        if result != "":
            result += " + "
        result += str(num_sum)
    
    return result