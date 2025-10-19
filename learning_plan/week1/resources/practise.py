#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@File:    practise.py
@Author:  Aslice
@Date:    2025/10/20 04:11
@Description:
"""

from typing import List, Optional


def sum_of_even_squares(numbers: List[int]) -> Optional[int]:
    '''
    **题目1：** 编写一个函数，接受一个整数列表作为参数，返回其中所有偶数的平方和。
    '''
    # 在这里编写你的代码
    sum = 0
    for i in numbers:
        if i % 2 == 0:
            sum += i ** 2
    return sum


def find_longest_string(strings: List[str]) -> str:
    '''
    **题目2：** 编写一个函数，接受一个字符串列表，返回其中最长的字符串。
    '''
    sum_str: str = ""
    for i in strings:
        if len(i) > len(sum_str):
            sum_str = i
    return sum_str


class Rectangle:
    '''
    定义一个名为 `Rectangle` 的类，具有以下属性和方法：
    - 属性：长度(length)和宽度(width)
    - 方法：计算面积(area)、计算周长(perimeter)、判断是否为正方形(is_square)
    '''

    def __init__(self, length: int, width: int) -> None:
        # 初始化代码
        self.length: int = length
        self.width: int = width

    def area(self) -> int:
        # 计算并返回面积
        return self.length * self.width

    def perimeter(self) -> int:
        # 计算并返回周长
        return (self.length + self.width) * 2

    def is_square(self) -> bool:
        # 判断是否为正方形，是则返回True，否则返回False
        if self.length == self.width:
            return True
        return False


def matrix_calculations(a: List[List[int]], b: List[List[int]], method: str) -> List[List[float]]:
    '''
    矩阵计算
    '''

    def _get_val(_row_index: int, _item_index: int, matrix: List[List[int]], default: int = 0) -> int:
        if _row_index > len(matrix):
            return default
        else:
            if _item_index > len(matrix[_row_index]):
                return default
            else:
                return matrix[_row_index][_item_index]

    # 矩阵初始化
    row_sum = max(len(a), len(b))
    col_sum = max(len(a[0]), len(b[0]))
    result = [[0.0 for _ in range(col_sum)] for _ in range(row_sum)]
    # 查找方法
    if method not in ["add", "subtract", "multiplication", "division"]:
        raise ValueError("无效的 方法(method)")
    for row_index, row in enumerate(result):
        for item_index, _ in enumerate(row):
            a_val = _get_val(row_index, item_index, a)
            b_val = _get_val(row_index, item_index, b)
            if method == "add":
                # 相加
                result[row_index][item_index] = a_val + b_val
            elif method == "subtract":
                # 相减
                result[row_index][item_index] = a_val - b_val
            elif method == "multiplication":
                # 相乘
                result[row_index][item_index] = a_val * b_val
            elif method == "division":
                # 相除
                if b_val == 0:
                    raise ValueError(f"除数不能为零 row:{row_index},col:{item_index}")
                result[row_index][item_index] = a_val / b_val
    return result

# 测试用例
if __name__ == '__main__':
    print(sum_of_even_squares([1, 2, 3, 4, 5, 6]))  # 应该输出 56 (2^2 + 4^2 + 6^2 = 4 + 16 + 36)
    print(find_longest_string(["cat", "dog", "elephant", "bat"]))  # 应该输出 "elephant"

    rect = Rectangle(5, 3)
    print(rect.area())  # 应该输出 15
    print(rect.perimeter())  # 应该输出 16
    print(rect.is_square())  # 应该输出 False

    square = Rectangle(4, 4)
    print(square.is_square())  # 应该输出 True

    '''
    给定两个向量 u = [2, 3, 1] 和 v = [1, -1, 4]，计算：
    向量加法: u + v
    向量点积: u · v
    向量u的模长
    '''
    A = [[1, 2],
         [3, 4]]

    B = [[5, 6],
         [7, 8]]
    print(matrix_calculations(A, B, "add"))
    print(matrix_calculations(A, B, "multiplication"))

    '''
    f(x) = 3x^2 + 2x - 5
    f(x) = sin(x) + cos(x)
    f(x, y) = x^2*y + 3xy^2，计算∂f/∂x和∂f/∂y
    '''
