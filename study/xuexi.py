# -*- coding: utf-8 -*-
import time, functools

'fang hua jie'

import sys


def test():
    args = sys.argv
    print(args, len(args))
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


# if __name__ == '__main__':
#    test()


def mul(x, *args):
    """
    :param x:
    :param args:
    :return:
    """
    s = x
    for i in args:
        s = s*i
    return s


print('mul(5) =', mul(5))  # 测试
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
    print('测试失败!')
elif mul(5, 6) != 30:
    print('测试失败!')
elif mul(5, 6, 7) != 210:
    print('测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        mul()
        print('测试失败!')
    except TypeError:
        print('测试成功!')


def metric(fn):
    """
    :param fn:
    :return:
    """
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        st = time.time()
        ff = fn(*args, **kw)
        et = time.time()
        print('%s executed in %s ms' % (fn.__name__, et-st))
        return fn(*args, **kw)
    return wrapper

# 测试
@metric
def fast(x, y):
    """
    :param x:
    :param y:
    :return:
    """
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    """
    :param x:
    :param y:
    :param z:
    :return:
    """
    time.sleep(0.1234)
    return x * y * z


f1 = fast(11, 22)
s1 = slow(11, 22, 33)
if f1 != 33:
    print('测试失败!')
elif s1 != 7986:
    print('测试失败!')
