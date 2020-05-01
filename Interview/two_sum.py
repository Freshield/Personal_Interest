# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: two_sum.py
@Time: 2020-04-29 12:42
@Last_update: 2020-04-29 12:42
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


class Solution(object):
    """
    找目标
    解法：
    找两数之和，a+b=c，b = c -a ，
    通过一个字典来记录数值，看是否可以找到c-a
    """
    def two_sum(self, input_list, target):
        """
        整体流程：
        1. 建立mem字典
        2. 遍历数字
        3. 如果字典中含有c-a的数值则返回True
        4. 否则放到字典中
        """
        # 1.
        mem = dict()
        # 2.
        for num in input_list:
            b = target - num
            if mem.get(b, None) is not None:
                return True

            mem[num] = 1

        return False


if __name__ == '__main__':
    input_list = [1,2,3,4,5]
    target = 7
    print(Solution().two_sum(input_list, target))