# -*- coding: utf-8 -*-
"""
通过代码对比解析Python的装饰器语法糖@的原理和实际运用

run_demo_1_x：通过场景对比理解Python的装饰器语法糖原理
run_demo_2_x：通过场景对比理解复杂的装饰器参数
"""

import logging


def print_logging_warning(func):
    """打印log的装饰器

    :param func: 被装饰的函数引用
    :return: 装饰过的函数引用
    """
    # 装饰过的函数
    def _decorated_func(*arg, **kwargs):
        logging.warning("== start to run function: {0}".format(func.func_name))
        result = func(*arg, **kwargs)
        logging.warning("== function {0} is done.".format(func.func_name))
        return result
    return _decorated_func


def print_demo_1():
    """未被装饰的函数"""
    print("print demo 1")


@print_logging_warning
def print_demo_1x():
    """被装饰的函数"""
    print("print demo 1")


def run_demo_1_1():
    """装饰器语法糖@效果"""
    print_demo_1x()


def run_demo_1_2():
    """装饰器调用原理展示"""
    new_func = print_logging_warning(print_demo_1)
    new_func()


def print_logging_msg(logging_level):
    """按log级别打印log信息的装饰器

    :param logging_level: logging.ERROR打印error信息，其余状态打印warning信息
    :return: 装饰过的函数引用
    """
    logging_func = logging.warning
    if logging_level == logging.ERROR:
        logging_func = logging.error

    # 外层的装饰器函数
    def _print_logging_msg(func):
        # 装饰过的函数
        def _decorated_func(*arg, **kwargs):
            logging_func("== start to run function: {0}".format(func.func_name))
            result = func(*arg, **kwargs)
            logging_func("== function {0} is done.".format(func.func_name))
            return result
        return _decorated_func
    return _print_logging_msg


@print_logging_msg(logging.ERROR)
def print_demo_2():
    print("print demo 2")


@print_logging_msg(logging.WARNING)
def print_demo_2x():
    print("print demo 2")


def run_demo_2_1():
    """装饰器参数展示1"""
    print_demo_2()


def run_demo_2_2():
    """装饰器参数展示2"""
    print_demo_2x()


if __name__ == "__main__":
    print("-" * 70)
    print("show demo")
    # 1-通过注释对比run_demo_1_1和run_demo_1_2的结果
    # run_demo_1_1()
    # run_demo_1_2()

    # 2-通过注释对比run_demo_2_1和run_demo_2_2的结果
    # run_demo_2_1()
    # run_demo_2_2()
