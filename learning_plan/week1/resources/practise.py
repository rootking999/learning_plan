from typing import List, Optional


def sum_of_even_squares(numbers:List[int])->Optional[int]:
    '''
    **题目1：** 编写一个函数，接受一个整数列表作为参数，返回其中所有偶数的平方和。
    '''
    # 在这里编写你的代码
    sum = 0
    for i in numbers:
        if i % 2 == 0:
            sum += i ** 2
    return sum

def find_longest_string(strings:List[str]) -> str:
    '''
    **题目2：** 编写一个函数，接受一个字符串列表，返回其中最长的字符串。
    '''
    sum_str:str = ""
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
    def __init__(self, length:int, width:int) -> None:
        # 初始化代码
        self.length:int = length    
        self.width:int = width    
    
    def area(self) -> int:
        # 计算并返回面积
         return self.length* self.width
    
    def perimeter(self) -> int:
        # 计算并返回周长
       return ( self.length+ self.width)*2
    
    def is_square(self) -> bool:
        # 判断是否为正方形，是则返回True，否则返回False
        if self.length== self.width:
            return True
        return False
# 测试用例
if __name__ == '__main__':
    print(sum_of_even_squares([1, 2, 3, 4, 5, 6]))  # 应该输出 56 (2^2 + 4^2 + 6^2 = 4 + 16 + 36)
    print(find_longest_string(["cat", "dog", "elephant", "bat"]))  # 应该输出 "elephant"

    rect = Rectangle(5, 3)
    print(rect.area())        # 应该输出 15
    print(rect.perimeter())   # 应该输出 16
    print(rect.is_square())   # 应该输出 False

    square = Rectangle(4, 4)
    print(square.is_square()) # 应该输出 True

