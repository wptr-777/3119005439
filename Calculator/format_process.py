from fractions import Fraction


class Convert:
    def std_fraction(answer):
        if (answer > 1 or answer < -1) and answer.denominator != 1:
            a_numerator = answer.numerator % answer.denominator
            a_denominator = answer.denominator
            a_right = Fraction(a_numerator, a_denominator)
            a_left = answer.numerator // answer.denominator
            result = str(a_left) + '\'' + str(a_right)
        else:
            result = str(answer)
        return result

    def std_output(formula):
        output = str()
        for item in formula:
            if isinstance(item, Fraction):
                output += Convert.std_fraction(item)
            elif isinstance(item, int):
                output += str(item)
            elif item == '+':
                output += ' + '
            elif item == '-':
                output += ' - '
            elif item == '*':
                output += ' x '
            elif item == '/':
                output += ' ÷ '
            else:
                output += item
        output += ' ＝ '
        return output

    def get_after_formula(formula):
        op_priority = {'(': 0, ')': 0, '+': 1, '-': 1, '*': 2, '/': 2}
        postfix_formula = list()
        op_list = list()
        for item in formula:
            if isinstance(item, int) or isinstance(item, Fraction):
                postfix_formula.append(item)
            elif item == '(':
                op_list.append(item)
            elif item == ')':
                while op_list[-1] != '(':
                    postfix_formula.append(op_list.pop())
                op_list.pop()  #
            else:
                while len(op_list) > 0 and op_priority[op_list[-1]] >= op_priority[item]:
                    postfix_formula.append(op_list.pop())
                op_list.append(item)

        while op_list:
            postfix_formula.append(op_list.pop())
        return postfix_formula
