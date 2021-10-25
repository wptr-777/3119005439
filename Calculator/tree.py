import os
import random
from fractions import Fraction
from calc import *
from op_file import My_file
from format_process import Convert


class Node:
    def __init__(self):
        self.type = 0
        self.operator = None
        self.number = None
        self.left = None
        self.right = None
        self.op_priority = {'+': 1, '-': 1, '*': 2, '/': 2}

    def get_answer(self):
        if self.type == 2:
            self.left.get_answer()
            self.right.get_answer()
            self.number = Calculator.eval_expr(
                self.operator, self.left.number, self.right.number)
        else:
            return

    def get_formula(self):
        formula = list()
        if self.type == 1:
            return [self.number]
        elif self.type == 2:
            if self.left.type == 2 and \
                    self.op_priority[str(self.operator)] > self.op_priority[str(self.left.operator)]:
                formula.append('(')
                formula += self.left.get_formula()
                formula.append(')')
            else:
                formula += self.left.get_formula()

            formula.append(self.operator)
            if self.right.type == 2 and \
                    self.op_priority[str(self.operator)] >= self.op_priority[str(self.right.operator)]:
                formula.append('(')
                formula += self.right.get_formula()
                formula.append(')')
            else:
                formula += self.right.get_formula()
            return formula


class My_Tree:
    def __init__(self):
        self.root = Node()
        self.op_list = ["+", "-", "*", "/"]
        self.type = [1, 2]
        self.middle_formula = list()
        self.after_formula = list()
        self.formula = list()
        self.answer = list()

    def create(self, num_range, number):
        num = 0
        while num < number:
            degree = random.choice([1, 2, 3])
            empty_node = [self.root]
            for _ in range(degree):
                node = random.choice(empty_node)
                empty_node.remove(node)
                node.operator = random.choice(self.op_list)
                node.type = 2
                node.left = Node()
                node.right = Node()
                empty_node.append(node.left)
                empty_node.append(node.right)

            for node in empty_node:
                node.type = 1
                num_type = random.choice(self.type)
                if num_type == 1:
                    node.number = random.randint(1, number)
                else:
                    node.number = Fraction(random.randint(1, num_range), random.randint(1, num_range))
            try:
                self.root.get_answer()
                self.middle_formula = self.root.get_formula()
                self.after_formula = Convert.get_after_formula(self.middle_formula)
                output = Convert.std_output(self.middle_formula)
                if isinstance(self.root.number, Fraction):
                    answer = Convert.std_fraction(self.root.number)
                else:
                    answer = self.root.number
                if answer in self.answer:
                    continue
                else:
                    self.formula.append(output)
                    self.answer.append(answer)
            except NegativeError:
                continue
            except ZeroDivisionError:
                continue
            else:
                num += 1
        return self.formula, self.answer
