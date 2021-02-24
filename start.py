from dice_class import *

number_of_players = 2
number_of_rounds = 3
number_of_queue = 15


def data_save(switch, lst):
    global pos, s
    if switch == "1":
        pos = 0
        s = dice.quantity_numbers(1, lst) * 1
    elif switch == "2":
        pos = 1
        s = dice.quantity_numbers(2, lst) * 2
    elif switch == "3":
        pos = 2
        s = dice.quantity_numbers(3, lst) * 3
    elif switch == "4":
        pos = 3
        s = dice.quantity_numbers(4, lst) * 4
    elif switch == "5":
        pos = 4
        s = dice.quantity_numbers(5, lst) * 5
    elif switch == "6":
        pos = 5
        s = dice.quantity_numbers(6, lst) * 6
    else:
        switch = switch.upper()
        if switch == "A":
            pos = 6
            s = dice.max_sum_one_pair_list(lst)
        elif switch == "B":
            pos = 7
            s = dice.sum_two_pairs(lst)
        elif switch == "C":
            pos = 8
            s = dice.sum_small_straight(lst)
        elif switch == "D":
            pos = 9
            s = dice.sum_big_straight(lst)
        elif switch == "E":
            pos = 10
            s = dice.sum_three(lst)
        elif switch == "F":
            pos = 11
            s = dice.sum_full(lst)
        elif switch == "G":
            pos = 12
            s = dice.sum_carriage(lst)
        elif switch == "H":
            pos = 13
            s = dice.sum_poker(lst)
        elif switch == "I":
            pos = 14
            s = dice.sum_all_elements(lst)
    return pos, s

def element_save():
    save = str(input("Czy chcesz zapisać dane [T/N]? "))
    if save in ['T', 't']:
        n = 0
        position = str(input("Wybierz pozycję: "))
        if position in ['1', '2', '3', '4', '5', '6', 'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd',
                        'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i']:
            pos, s = data_save(position, random)
            sc.update(sc.score, _player, pos, s)
            sc.print(sc.score, 1)
        else:
            print("Niewłaściwy wybór!")


def create_players(value):
    players = []
    for x in range(value):
        name = str(input('Podaj imie gracza: '))
        players.append(name)
    return players


global random

# player = create_players(number_of_players)

dice = Dice()
sc = Score(number_of_players)
print('Początkowy stan gry: ')
sc.print(sc.score, 1)

_queue = 0
while _queue != number_of_queue:
    # print('Kolejka = ', _queue + 1)

    _player = 0
    while _player != number_of_players:
        # print('--- Zawodnik = ', _player + 1)

        _round = 0
        while _round != number_of_rounds:
            # print("--- --- Runda = ", _round + 1)
            print('--- --- --- --- --- --- --- --- --- --- --- ---')
            print('Kolejka = ', _queue + 1, ' |  Zawodnik = ', _player + 1, ' |  Runda = ', _round + 1)
            print('--- --- --- --- --- --- --- --- --- --- --- ---')

            if _round == 0:
                random = dice.many_dice_roll()
                random.sort()

            index = dice.numbers_counter_list(random)

            print("wylosowane: ", random, " -> wystąpienia: ", index)
            print("--- ---")
            dice.score_report(random)
            print("--- ---")

            change_dice = str(input('Czy ponawiasz losowanie [T/N]? '))

            if change_dice in ['T', 't']:
                change = int(input('Iloma kostkami chesz ponownie rzucić? '))

                if change in range(1, 5):
                    selected_list = []

                    while change != 0:
                        index_change = int(input('Wskaż pozycję kostki do ponownego rzutu [1..5]: '))
                        selected_list.append(index_change - 1)
                        change -= 1

                    numbers = dice.selected_dice_roll(random, selected_list)
                    numbers.sort()

                else:
                    print("Błędna liczba kostek!")

            else:
                # zapis
                save = str(input("Czy chcesz zapisać dane [T/N]? "))

                if save in ['T', 't']:
                    n = 0
                    position = str(input("Wybierz pozycję: "))

                    if position in ['1', '2', '3', '4', '5', '6', 'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd',
                                    'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i']:
                        pos, s = data_save(position, random)
                        sc.update(sc.score, _player, pos, s)
                        sc.print(sc.score, 1)
                        break
                    else:
                        print("Niewłaściwy wybór!")
                else:
                    break

            _round += 1
            if _round == 3:
                print('Koniec rundy')
                save = str(input("Czy chcesz zapisać dane [T/N]? "))

                if save in ['T', 't']:
                    n = 0
                    position = str(input("Wybierz pozycję: "))

                    if position in ['1', '2', '3', '4', '5', '6', 'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd',
                                    'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i']:
                        pos, s = data_save(position, random)
                        sc.update(sc.score, _player, pos, s)
                        sc.print(sc.score, 1)
                        break
                    else:
                        print("Niewłaściwy wybór!")

        _player += 1

    _queue += 1

sc.print(sc.score, 1)
