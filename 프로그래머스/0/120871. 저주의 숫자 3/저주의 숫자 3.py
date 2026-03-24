def solution(n):
    number = 0
    count = 0

    while count < n:
        number += 1

        if number % 3 == 0 or '3' in str(number):
            continue

        count += 1

    return number