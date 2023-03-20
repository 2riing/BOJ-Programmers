def solution(id_pw, db):
    answer = ''
    for d in db:
        id, pw = id_pw
        if id == d[0] and pw == d[1]:
            answer = 'login'
            return answer
        elif id == d[0] and pw != d[1]:
            answer = 'wrong pw'
        else:
            answer = 'fail'
    return answer
