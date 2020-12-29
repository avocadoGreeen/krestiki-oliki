import pickle


def saves():
    dict_strok = {}
    dict_stolb = {}
    dict_element_win = {}

    name = 'Tester'
    k_str = 3
    k_stolb = 3
    count_win = 3

    # добавление в словарь имени(ключ) - строк/столбцов/подряд_победы(значение)
    dict_strok[str(name)] = k_str
    dict_stolb[str(name)] = k_stolb
    dict_element_win[str(name)] = count_win

    # запись ключ-значение в словари
    with open('field', 'wb') as save:
        pickle.dump(dict_strok, save)
        pickle.dump(dict_stolb, save)
        pickle.dump(dict_element_win, save)

    # проверка записей в файле
    with open('field', 'rb') as save:
        dict_strok = pickle.load(save)
        dict_stolb = pickle.load(save)
        dict_element_win = pickle.load(save)

    print(dict_strok)
    print(dict_stolb)
    print(dict_element_win)


saves()
