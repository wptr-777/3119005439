import operator
from fractions import Fraction


class NegativeError(Exception):
    def __init__(self):
        super(NegativeError, self).__init__()


class Calculator:
    def eval_expr(op_code, a, b):
        answer = 0
        if op_code == "+":
            answer = operator.add(a, b)
        elif op_code == "-":
            if operator.lt(a, b):
                raise NegativeError()
            else:
                answer = operator.sub(a, b)
        elif op_code == "*":
            answer = operator.mul(a, b)
        elif op_code == "/":
            if b == 0:
                raise ZeroDivisionError
            answer = operator.truediv(a, b)
            if isinstance(answer, float):  # if answer is float/double turn to Fraction
                answer = operator.truediv(Fraction(a), Fraction(b))
        return answer

    def calc_score(user_ans, ans_list):  # calc correct rate
        correct = list()
        wrong = list()
        length = len(user_ans)
        for i, u, ans in zip(range(1, length + 1), user_ans, ans_list):
            if u == ans:
                correct.append(i)
            else:
                wrong.append(i)
        return correct, wrong
