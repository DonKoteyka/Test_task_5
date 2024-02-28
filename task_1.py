import random

def method_1(num: int) -> bool:
    span = range(2, 10000000, 2)
    """
    создаём список чётных чисел и потом просто проверяем
    из минусов при вызове каждый раз создаётся переменная с большим количеством значений
    (можно оптимизировать создав span 1 раз и передав его как аргумент)
    главный минус заключается в том, что работает на ограниченном диапазоне чисел
    """

    if num in span:
        return True
    else:
        return False


def method_2(num: int) -> bool:
    """
    Этот метод использует побитовую операцию AND с числом 1, чтобы проверить младший бит числа.
    Если результат равен 0, то число четное, иначе - нечетное.
    из плюсов то, что не происходит вычислений, только сравнение и то один раз, следовательно метод максимально быстр
    из минусов он был нагуглин.
    """
    if num & 1 == 0:
        return True
    else:
        return False

def method_3(num: int) -> bool:
    """
    компиляция метода 1 и 2 болше операций чем в 2, но без ограничений
    """
    span = range(0, 12, 2)

    if int(str(num)[-1]) in span:
        return True
    else:
        return False

def method_4(num: int) -> bool:
    """
    проверка последнего числа на чётность методом вычислений
    из плюсов всё ещё не много действий (меньше, чем делить до результата всю сумму),
    но больше чем в предыдущих методах
    """
    string = str(num)
    end = int(string[-1])
    result = end / 2
    if num == 0:
        return False
    elif result == int(result):
        return True
    else:
        return False
    
def method_5(num: int) -> bool:
    """
    аналогично классисческому методу, делим на 2 если результат целое число, то исходное число было чётное
    """
    result = num / 2
    if num == 0:
        return False
    elif result == int(result):
        return True
    else:
        return False


def method_pattrn(num: int) -> bool:
    """
    контрольный метод
    """
    return num % 2 == 0



if __name__ == "__main__":
    func = (method_1, method_2, method_3, method_4, method_5)
    num = random.randint(1, 99999)
    print(num)
    for i in func:
        print(i(num))

