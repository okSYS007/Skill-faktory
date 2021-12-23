#Выполните реверсирование строк файла (перестановка строк файла в обратном порядке).


def main():

    with open('input.txt', 'r', encoding='utf8') as input_file:
        with open('output.txt', 'w', encoding='utf8') as output_file:
            for line in reversed(input_file.readlines()):
                output_file.write(line)


if __name__ == '__main__':
    main()

