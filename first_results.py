import pickle


def res_game():
    dict_games = {}  # словарь количества игр
    dict_win = {}  # словарь побед
    dict_lose = {}  # словарь поражений
    dict_tie = {}  # словарь ничьей

    name = 'Tester'
    games = 1
    win = 1
    lose = 0
    tie = 0

    # добавление ключ-значение в словари
    dict_games[str(name)] = games
    dict_win[str(name)] = win
    dict_lose[str(name)] = lose
    dict_tie[str(name)] = tie

    # запись словарей в файл
    with open('results', 'wb') as save2:
        pickle.dump(dict_games, save2)
        pickle.dump(dict_win, save2)
        pickle.dump(dict_lose, save2)
        pickle.dump(dict_tie, save2)

    #
    with open('results', 'rb') as save2:
        dict_games = pickle.load(save2)
        dict_win = pickle.load(save2)
        dict_lose = pickle.load(save2)
        dict_tie = pickle.load(save2)

    print('Игры : ', dict_games)
    print('Победы : ', dict_win)
    print('Поражения : ', dict_lose)
    print('Ничья : ', dict_tie)


res_game()
