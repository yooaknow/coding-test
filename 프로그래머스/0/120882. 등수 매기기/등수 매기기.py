def solution(score):
    sums = [s[0] + s[1] for s in score]
    answer = []

    for i in sums:
        rank = 1
        for j in sums:
            if j > i:
                rank += 1
        answer.append(rank)

    return answer