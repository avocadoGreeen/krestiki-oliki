import random
import pickle

def sign_in():
    global name
    global k_strok
    global k_stolb
    global count_win
    global q_first
    global game_board
    # регистрация/вход, загрузка предыдущего поля/настройка своего поля
    q_first = input("Добро пожаловать в игру крестики-нолики! Вы здесь в первый раз? (+/-): ")
    while q_first != '+' and q_first != '-':
        q_first = input("Добро пожаловать в игру крестики-нолики! Вы здесь в первый раз? (+/-): ")

    if q_first == "+":
        with open('field', 'rb') as save:  # проверка наличия имени в файле
            dict_strok = pickle.load(save)
        name = input("Как к вам можно обращаться? ")
        for i in dict_strok:
            while name in dict_strok:
                print("Данное имя уже занято, пожалуйста, попробуйте еще раз")
                name = input("Как к вам можно обращаться? ")
        print("Приятно познакомиться," + str(name).title() + "!")
        print("Вы можете выбрать настройки своего поля: количество столбцов строк поля,"
              "в котором хотите сыграть и количество знаков в ряд, необходимые для победы.")

        while True:
            try:
                k_strok = int(input('Введите количество строк в поле: '))  # кол-во строк # размер поля
                break
            except ValueError:
                print("Ошибка ввода.")
        while True:
            try:
                k_stolb = int(input('Введите количество столбцев в поле: '))
                break
            except ValueError:
                print("Ошибка ввода.")
        while True:
            try:
                count_win = int(input('Введите количество символов для победы: '))
                break
            except ValueError:
                print("Ошибка ввода.")
        # заполнение массива пустыми значениями
        game_board = [[" " for j in range(k_stolb)] for i in range(k_strok)]

    elif q_first == "-":
        with open('results', 'rb') as save2:  # проверка имени в словаре dict_games - results
            dict_games = pickle.load(save2)
        name = input("Как к вам можно обращаться? ")
        for i in dict_games:
            while name not in dict_games:
                print("Данное имя не найдено, попробуйте ввести имя еще раз")
                name = input("Как к вам можно обращаться? ")
        print("С возращением, " + str(name).title() + "!")

        with open('field', 'rb') as save:  # проверка этого же имени в файле field
            dict_strok = pickle.load(save)
        if name in dict_strok:
            field_save = input(name.title() + ", хотите загрузить настройки поля с предыдущей игры?(+/-) ")
            while field_save != '+' and field_save != '-':
                field_save = input(name.title() + ", хотите загрузить настройки поля с предыдущей игры?(+/-) ")

            if field_save == "+":
                with open('field', 'rb') as save:
                    dict_strok = pickle.load(save)
                    dict_stolb = pickle.load(save)
                    dict_win = pickle.load(save)
                    k_strok = dict_strok[str(name)]
                    k_stolb = dict_stolb[str(name)]
                    count_win = dict_win[str(name)]
                # заполнение массива пустыми значениями
                game_board = [[" " for j in range(k_stolb)] for i in range(k_strok)]

            elif field_save == "-":
                while True:
                    try:
                        k_strok = int(input('Введите количество строк в поле: '))  # кол-во строк # размер поля
                        break
                    except ValueError:
                        print("Ошибка ввода.")
                while True:
                    try:
                        k_stolb = int(input('Введите количество столбцев в поле: '))
                        break
                    except ValueError:
                        print("Ошибка ввода.")
                while True:
                    try:
                        count_win = int(input('Введите количество символов для победы: '))
                        break
                    except ValueError:
                        print("Ошибка ввода.")
                # заполнение массива пустыми значениями
                game_board = [[" " for j in range(k_stolb)] for i in range(k_strok)]

        else:
            while True:
                try:
                    k_strok = int(input('Введите количество строк в поле: '))  # кол-во строк # размер поля
                    break
                except ValueError:
                    print("Ошибка ввода.")
            while True:
                try:
                    k_stolb = int(input('Введите количество столбцев в поле: '))
                    break
                except ValueError:
                    print("Ошибка ввода.")
            while True:
                try:
                    count_win = int(input('Введите количество символов для победы: '))
                    break
                except ValueError:
                    print("Ошибка ввода.")
            # заполнение массива пустыми значениями
            game_board = [[" " for j in range(k_stolb)] for i in range(k_strok)]





# инструкция
def instruction(game_board):
    with open('results', 'rb') as save2:
        dict_games = pickle.load(save2)
    if name in dict_games:
        q_instruction = input('Хотите посмотреть инструкцию?(+/-) ')
        if q_instruction == '+':
            print("""
    Правила игры просты:
    Игроки по очереди ставят на свободные клетки поля, которое можно настроить,
    знаки(один всегда крестики, другой всегда нолики). Знак можно выбрать.
    Первый, выстроивший в ряд выбранное количество элементов своих фигуры по вертикали,
    горизонтали или диагонали, выигрывает.
                """)
            board(game_board)
            input("Чтобы начать игру, нажмите клавишу Enter...")
        else:
            board(game_board)
    else:
        print("""
        Правила игры просты:
        Игроки по очереди ставят на свободные клетки поля, которое можно настроить,
        знаки(один всегда крестики, другой всегда нолики). Знак можно выбрать.
        Первый, выстроивший в ряд выбранное количество элементов своих фигуры по вертикали,
        горизонтали или диагонали, выигрывает.
            """)
        board(game_board)
        input("Чтобы начать игру, нажмите клавишу Enter...")


# поле
def board(game_board):
    # печать номеров столбцев
    i = 0
    print(" ", end='')
    while i < (len(game_board[0]) * 2 + 1):
        if i % 2 == 0:
            print(" ", end='')
        else:
            print(i // 2 + 1, end='')
        i += 1
    print(" ")

    # печать номеров строки
    i = 0
    while i < len(game_board):
        print(i + 1, end='')
        j = 0
        # печать строк
        while j < (len(game_board[i]) * 2 + 1):
            if j % 2 == 0:
                print("|", end='')
            else:
                print(game_board[i][j // 2], end='')
            j += 1
        print(" ")
        i += 1


# новая доска
def new_board(game_board):
    for i in range(k_strok):
        for j in range(k_stolb):
            if game_board[i][j] == "X" or game_board[i][j] == "O":
                game_board[i][j] = ' '


# выбор знака
def choose_symbol():
    global sign_of_user
    global sign_of_computer
    sign_of_computer = ''
    sign_of_user = input('Каким знаком хотите играть? (X или O): ').upper()
    if sign_of_user == 'X':
        print('Можете начинать игру, ход Ваш.')
        sign_of_computer = 'O'
    elif sign_of_user == 'O':
        print('Надо было выбирать Х) Ваш первый ход забрал искусственный интеллект!')
        sign_of_computer = 'X'
    else:
        print('Вы ошиблись, попробуйте еще раз')
        choose_symbol()


# ход и свободные места человека
def move_user(game_board):
    stroka = int(input("Введите номер строки: "))
    stolbets = int(input("Введите номер столбца: "))
    while stroka > k_strok or stolbets > k_stolb:
        print('Неккоректный ввод строки или столбца. Попробуйте еще раз')
        stroka = int(input("Введите номер строки: "))
        stolbets = int(input("Введите номер столбца: "))
    while game_board[stroka - 1][stolbets - 1] == "X" or game_board[stroka - 1][stolbets - 1] == "O":
        print("Уже занято! Попробуйте еще раз.")
        stroka = int(input("Введите номер строки: "))
        stolbets = int(input("Введите номер столбца: "))
    else:
        game_board[stroka - 1][stolbets - 1] = sign_of_user


# ход компьютера
def move_computer(game_board):
    c = True
    while c:
        a = random.randint(0, k_strok - 1)
        b = random.randint(0, k_stolb - 1)
        if game_board[a][b] != 'X' \
                and game_board[a][b] != 'O':
            game_board[a][b] = sign_of_computer
            c = False
        else:
            continue

def first_move_comp(game_board):
    if sign_of_computer == 'X':
        move_computer(game_board)
        board(game_board)

# проверка победы
def who_wins(symbol):
    for j in range(k_stolb):
        count_symbol = 0
        for i in range(k_strok):
            if game_board[i][j] == symbol:
                count_symbol += 1
                if count_symbol == count_win:
                    return True
            else:
                count_symbol = 0
    for i in range(k_strok):
        count_symbol = 0
        for j in range(k_stolb):
            if game_board[i][j] == symbol:
                count_symbol += 1
                if count_symbol == count_win:
                    return True
            else:
                count_symbol = 0
    # проверка главной диагонали 3x3
    count_symbol = 0
    for i in range(k_strok):
        for j in range(k_stolb):
            if game_board[i][j] == symbol:
                if i == j:
                    count_symbol += 1
                    if count_symbol == count_win:
                        return True
                    break
                else:
                    count_symbol = 0
    # проверка побочной диагонали 3x3
    count_symbol = 0
    for i in range(k_strok):
        for j in range(k_stolb):
            if game_board[i][j] == symbol:
                if i + j == k_strok - 1:
                    count_symbol += 1
                    if count_symbol == count_win:
                        return True
                    break
                else:
                    count_symbol = 0

    # проверка главной диагонали слева-направо
    for k in range(k_stolb - count_win + 1):
        count_symbol1 = 0
        count_symbol2 = 0
        for i in range(k_strok):
            for j in range(k_stolb):
                if game_board[i][j] == symbol:
                    if i == j + k:  # столбец + 1
                        count_symbol1 += 1
                        if count_symbol1 == count_win:
                            return True
                        break

                    if i + k == j:  # строка + 1
                        count_symbol2 += 1
                        if count_symbol2 == count_win:
                            return True
                        break
                    else:
                        count_symbol2 = 0

    # проверка побочной диагонали справа налево
    for line in range(k_stolb - count_win + 1):
        for k in range(k_stolb - count_win + 1):
            count_symbol = 0
            for i in range(k_strok - line):
                if i + k == k_stolb:
                    break
                else:
                    if game_board[i + line][k_stolb - i - k - 1] == symbol:
                        count_symbol += 1
                        if count_symbol == count_win:
                            return True
                    else:
                        count_symbol = 0

    return False


# ничья
def tie(game_board):
    count_symbol = 0
    count_tie = k_strok * k_stolb
    for i in range(k_strok):
        for j in range(k_stolb):
            if game_board[i][j] == "X" or game_board[i][j] == "O":
                count_symbol += 1
                if count_symbol == count_tie:
                    return True
    return False


# игры, победы, поражения, ничья
def results_game():
    if q_first == '+':
        games = 0
        win = 0
        lose = 0
        tie = 0
        with open('results', 'rb') as save2:
            dict_games = pickle.load(save2)
            dict_win = pickle.load(save2)
            dict_lose = pickle.load(save2)
            dict_tie = pickle.load(save2)
    else:
        with open('results', 'rb') as save2:
            dict_games = pickle.load(save2)
            dict_win = pickle.load(save2)
            dict_lose = pickle.load(save2)
            dict_tie = pickle.load(save2)
            games = dict_games[str(name)]
            win = dict_win[str(name)]
            lose = dict_lose[str(name)]
            tie = dict_tie[str(name)]

    if who_wins(sign_of_user):
        games += 1
        win += 1
    elif who_wins(sign_of_computer):
        games += 1
        lose += 1
    else:
        games += 1
        tie += 1

    dict_games.update({str(name): games})
    dict_win.update({str(name): win})
    dict_lose.update({str(name): lose})
    dict_tie.update({str(name): tie})

    with open('results', 'wb') as save2:
        pickle.dump(dict_games, save2)
        pickle.dump(dict_win, save2)
        pickle.dump(dict_lose, save2)
        pickle.dump(dict_tie, save2)


# сохранение настроек поля
def saves():
    # выгружаем данные из файла
    with open('field', 'rb') as save:
        dict_strok = pickle.load(save)
        dict_stolb = pickle.load(save)
        dict_element_win = pickle.load(save)

    # обновление словаря
    dict_strok.update({str(name): k_strok})
    dict_stolb.update({str(name): k_stolb})
    dict_element_win.update({str(name): count_win})

    # обновление данных в файле
    with open('field', 'wb') as save:
        pickle.dump(dict_strok, save)
        pickle.dump(dict_stolb, save)
        pickle.dump(dict_element_win, save)

# заполнение массива пустыми значениями


def main():
    sign_in()
    instruction(game_board)
    choose_symbol()
    first_move_comp(game_board)
    while True:
        move_user(game_board)
        board(game_board)
        if who_wins(sign_of_user):
            print('Поздравляю, вы выйграли!')
            break
        if tie(game_board):
            print("Ничья.")
            break
        move_computer(game_board)
        board(game_board)
        if who_wins(sign_of_computer):
            print('Искусственный интеллект победил!')
            break
        if tie(game_board):
            print("Ничья.")
            break
    results_game()
    save_me = input('Сохранить настройки поля для следующей игры?(+/-): ')
    if save_me == "+":
        saves()
        print("Ваши данные успешно сохранены.")
    view_results = input('Хотите посмотреть статистику игры? (+/-) ')
    while view_results != '+' and view_results != '-':
        view_results = input('Хотите посмотреть статистику игры? (+/-) ')
    if view_results == '+':
        with open('results', 'rb') as save2:
            dict_games = pickle.load(save2)
            dict_win = pickle.load(save2)
            dict_lose = pickle.load(save2)
            dict_tie = pickle.load(save2)
        print('Игры: ', dict_games)
        print('Победы: ', dict_win)
        print('Поражения', dict_lose)
        print('Ничья: ', dict_tie)
        print('До скорой встречи!')
        input()
    else:
        print('До скорой встречи!')
        input()


main()
