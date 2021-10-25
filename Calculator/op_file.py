class My_file:
    def save_file(expr_set, ans_set, expr_file, ans_file):
        index = 0
        with open(expr_file, 'w+', encoding='utf-8') as e_file, \
                open(ans_file, 'w+', encoding='utf-8') as a_file:
            e_file.write('+' + '-' * 6 + '+' + '-' * 38 + '+' + '\n')
            e_file.write('|' + 'NO'.center(6, ' ') + '|' + 'Arithmetic'.center(38, ' ') + '|\n')
            e_file.write('+' + '-' * 6 + '+' + '-' * 38 + '+' + '\n')
            a_file.write('+' + '-' * 6 + '+' + '-' * 12 + '+' + '-' * 38 + '+' + '\n')
            a_file.write(
                '|' + 'NO'.center(6, ' ') + '|' + 'Answer'.center(12, ' ') + '|' + 'Arithmetic'.center(38, ' ') + '|\n')
            a_file.write('+' + '-' * 6 + '+' + '-' * 12 + '+' + '-' * 38 + '+' + '\n')

            for ans, content in zip(ans_set, expr_set):
                index += 1
                e_file.write('|' + str(index).center(6, ' ') + '|' + str(content).center(37, ' ') + '|\n')
                a_file.write(
                    '|' + str(index).center(6, ' ') + '|' + str(ans).center(12, ' ') + '|'\
                    + str(content).center(37,
                                          ' ') + '|' + '\n')
            e_file.write('+' + '-' * 6 + '+' + '-' * 38 + '+' + '\n')
            a_file.write('+' + '-' * 6 + '+' + '-' * 12 + '+' + '-' * 38 + '+' + '\n')
        print("Save successfully！")

    def save_grade_file(grade_file, correct, wrong):
        print("Saving the grade")
        with open(grade_file, 'w+', encoding='utf-8') as g_file:
            g_file.write("{:<9}".format("Correct:") + str(len(correct)) + str(correct) + '\n')
            g_file.write("{:<9}".format("Wrong:") + str(len(wrong)) + str(wrong) + '\n')
        print("Success!")
