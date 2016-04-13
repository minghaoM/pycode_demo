# -*- coding: utf-8 -*-
"""
基于对象的Python语言，通过一些研究方法type，dir，__mro__了解一些内部对象
迭代器协议：
    __iter__()返回该对象对应的迭代器对象，如list，tuple，dict等
    迭代器对象的next()方法
    for语句通过__iter__()方法获取迭代器对象，并调用迭代器对象的next()方法循环获取数据
    Python交互界面下演示list，tuple的__iter__()方法返回的对象和next
yield机制：
    包含yield语句的函数返回的是一个generator对象
    generator方便支持迭代器协议
    相比list，tuple等原生对象，在检索时才被赋值，省内存，性能好

对比空间占用和性能
    python -m timeit -n 1000 "a=[i for i in range(1000)]"
    python -m timeit -n 1000 "a=(i for i in range(1000))"
    python -m timeit -n 1000 "a=(i for i in xrange(1000))"
    使用sys.sizeof对比range(1000)和xrange(1000)的空间大小
"""


def gen1():
    yield 2


def gen2():
    yield 2
    yield 3


def gen3():
    while True:
        yield 2


def demo1():
    a = gen1()
    print("a is {0}".format(a))
    """
    print(type(a))
    print(type(a).__mro__)
    print(dir(a))
    """
    print("get next")
    print(a.next())
    print("get next again")
    print(a.next())
    """
    index = 0
    for item in a:
        print("index is:{0}".format(index))
        index += 1
        if index >= 10:
            break
        print("item is {0}".format(item))
    """


def demo2():
    a = gen3()
    print("a is {0}".format(a))
    index = 0
    for item in a:
        print("index is:{0}".format(index))
        index += 1
        if index >= 10:
            break
        print("item is {0}".format(item))


def demo3():
    a = list(gen2())
    print(a)


if __name__ == "__main__":
    print("### test")
    # print("### demo1")
    # demo1()
    # print("### demo2")
    # demo2()
    demo3()
