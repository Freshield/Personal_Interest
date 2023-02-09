# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: print_tree.py
@Time: 2020-04-29 12:50
@Last_update: 2020-04-29 12:50
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


class Solution():
    def __init__(self):
        self.FIFO = []
        self.last_node = None

    def print_tree(self, node):
        """
        整体流程：
        1. 放入根节点
        2. 遍历FIFO的长度
        2. 把节点pop出来
        3. 打印节点的val
        4. 压入节点的左右
        5. 结束条件如果FIFO为空则结束
        """
        # 1. 放入根节点
        self.FIFO.append(node)
        while True:
            if len(self.FIFO) == 0:
                break
            # 2. 把节点pop出来
            this_node = self.FIFO.pop(0)
            # 3. 打印节点的val
            print(this_node.val)
            # 4. 压入节点的左右
            if this_node.left is not None:
                self.FIFO.append(this_node.left)
                self.last_node = this_node.left
            if this_node.right is not None:
                self.FIFO.append(this_node.right)
                self.last_node = this_node.right




