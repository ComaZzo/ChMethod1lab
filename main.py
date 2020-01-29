import math

epsilon = 10 ** (-15)

if __name__ == '__main__':
    print('Epsilon: {:.15f}'.format(epsilon))
    print('Enter value of x:')
    try:
        x = float(input())
    except:
        print('Error input value')
        exit(1)

    theory_result = (1 / (4 * math.pi * x**4)) - \
                    (math.pi / (4 * x ** 2)) * (1 / math.tan(math.pi * x)) * (1 / math.tanh(math.pi * x))

    result = 0
    k = 1
    for k in range(1, 100000):
        try:
            temp = (k / (k ** 4 - x ** 4)) * (1 / math.tanh(k * math.pi))
        except Exception as exc:
            print('-' * 40)
            print(f'Exception on {k} iteration')
            print('-' * 40)
            print('Error: ' + str(exc))
            break
        result += temp
        if k % 5 == 0:
            print('[{}]: {:.16f} | {:.16f}'.format(k, result, temp))
        if abs(theory_result - result) <= epsilon:
            print(f'Achieved result at {k} iteration')
            break
        k+=1
    else:
        print('Epsilon has not been achieved')

    print('Sum of range from iterations:              {:+.16f}'.format(result))
    print('Theory result from calculating right part: {:+.16f}'.format(theory_result))
