import os
import argparse
from tree import My_Tree
from op_file import My_file
from calc import Calculator


if __name__ == '__main__':
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('-n', dest='amount', type=int, default=10, help='题目的数量')
    my_parser.add_argument('-r', dest='range', type=int, default=10, help='生成数字的范围')
    my_args = my_parser.parse_args()
    q_path = os.path.join(os.getcwd(), 'Questions.txt')
    a_path = os.path.join(os.getcwd(), 'Answers.txt')
    s_path = os.path.join(os.getcwd(), 'Score.txt')
    print("Welcome to My calc program!")
    t = My_Tree()
    user_answers = list()
    generatives, answers = t.create(my_args.range, my_args.amount)                      # 题目以及答案的生成
    My_file.save_file(generatives, answers, q_path, a_path)             # 题目文件以及答案文件的生成
    for i in range(my_args.amount):
        print(generatives[i], end='')
        answer = input()
        user_answers.append(answer)
    correct, wrong = Calculator.calc_score(user_answers, answers)                   # calc score
    My_file.save_grade_file(s_path, correct, wrong)                              # save answer
