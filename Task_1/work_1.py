def discriminant(a, b, c):
    dic = b**2-4*a*c
    return dic


def solution(a, b, c):
    dic = discriminant(a, b, c)
    if dic < 0:
        return "корней нет"
    else:
        x1 = (-b + dic ** 0.5)/(2 * a)
        x2 = (-b - dic ** 0.5)/(2 * a)
        if x1 == x2:
            return x1
        else:
            return x1, x2


if __name__ == '__main__':
    print(solution(1, 8, 15))
    print(solution(1, -13, 12))
    print(solution(-4, 28, -49))
    print(solution(1, 1, 1))
