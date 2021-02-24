from random import randint


class Player(object):
    def __init__(self, _name):
        self.name = _name


class Score(object):
    def __init__(self, _players=1, _queue=15):
        self.number_of_players = _players
        self.number_of_queue = _queue
        self.score = [[0] * self.number_of_queue for i in range(self.number_of_players)]

    def reset(self, lst):
        for x in range(self.number_of_queue):
            for y in range(self.number_of_players):
                lst[y][x] = 0

    @staticmethod
    def bonus(lst):
        value = sum([j for i, j in enumerate(lst) if i < 6])
        if value == 63:
            results = 0
        elif value > 63:
            results = 20
        else:
            results = -10
        return results

    @staticmethod
    def sum_figure(self, lst):
        value = sum([j for i, j in enumerate(lst) if i > 6])
        return value

    def print(self, lst, switch=0):
        for i in range(0, self.number_of_players):
            if switch == 0:
                print(lst[i])
            else:
                #  print(f'Player - {i}:', lst[i], f' --> {sum(lst[i])}')
                w1 = self.sum_figure(self, lst[i])
                w2 = self.bonus(lst[i])
                w = w1 + w2
                print(f'Player - {i}:', lst[i], f' --> {w1}', f' + {w2} = {w}')

    def update(self, lst, player, queue, value):
        try:
            if (player in range(0, self.number_of_players)) | (queue in range(0, self.number_of_queue)):
                lst[player][queue] = value
        except IndexError:
            print('Parametr poza zakresem!')
            exit()


class Dice(object):
    def __init__(self):
        self.side = 6
        self.dice = 5

        # zwraca wynik rzutu jedną kostką

    def one_dice_roll(self):
        value_one_dice_roll = randint(1, self.side)
        return value_one_dice_roll

    # rzut wieloma kostkami
    def many_dice_roll(self):
        list_many_dice_roll = []
        for index in range(self.dice):
            list_many_dice_roll.append(self.one_dice_roll())
        return list_many_dice_roll

    # rzut wybranymi kostkami
    def selected_dice_roll(self, roll_list, selected_list):
        for index in selected_list:
            roll_list[index] = self.one_dice_roll()
        return roll_list

    # lista wystąpień poszczególnych liczb
    def numbers_counter_list(self, lst):
        results = []
        for index in range(1, self.side + 1):
            results.append(lst.count(index))
        return results

    # lista wystąpień poszczególnych liczb - słownik
    def numbers_counter_dict(self, lst):
        dict = {}
        for index in range(1, self.side + 1):
            element = lst.count(index)
            dict[index] = element
        return dict

    # sprawdza czy w liście wylosowanych liczb jest podany numer
    @staticmethod
    def check_number(number, lst):
        if number in lst:
            return True
        else:
            return False

    # zlicza ilość takich samych liczb
    @staticmethod
    def quantity_numbers(number, lst):
        if number in lst:
            return lst.count(number)
        else:
            return 0

    # sprawdza czy jest jedna para liczb
    def check_one_pair(self, lst):
        lst = self.numbers_counter_list(lst)
        v = 0
        for i in lst:
            if i % 2 == 0:
                v += i
            else:
                v += i - 1
        if v == 2 or v == 4:
            return True
        else:
            return False

    # sprawdza czy są dwie pary: pary mogą być takie same
    def check_two_pairs(self, lst):
        lst = self.numbers_counter_list(lst)
        v = 0
        for i in lst:
            if i % 2 == 0:
                v += i
            else:
                v += i - 1
        if v == 4:
            return True
        else:
            return False

    # sprawdza czy jest mały strit, czyli suma[1 ,2 ,3 ,4 ,5] = 15
    def check_small_straight(self, lst):
        sum_elements = sum([i for i in lst])  # suma elementów listy
        lst = self.numbers_counter_list(lst)
        values = sum([i for i in lst if i == 1])
        if sum_elements == 15 and values == 5:
            value = True
        else:
            value = False
        return value

    # sprawdza czy jest duży strit, czyli suma[2 ,3 ,4 , 5, 6] = 20
    def check_big_straight(self, lst):
        sum_elements = sum([i for i in lst])
        lst = self.numbers_counter_list(lst)
        values = sum([i for i in lst if i == 1])
        if sum_elements == 20 and values == 5:
            value = True
        else:
            value = False
        return value

    # sprawdza czy jest cokolwiek (szystkie różne)
    def check_chance(self, lst):
        sum_elements = sum([i for i in lst])
        lst = self.numbers_counter_list(lst)
        values = sum([i for i in lst if i == 1])
        if (sum_elements != 15 or sum_elements != 20) and values == 5:
            value = True
        else:
            value = False
        return value

    # sprawdza czy jest trójka
    def check_three(self, lst):
        lst = self.numbers_counter_list(lst)
        if (3 in lst) or (4 in lst) or (5 in lst):
            return True
        else:
            return False

    # sprawdza czy jest full: trójka i para
    def check_full(self, lst):
        lst = self.numbers_counter_list(lst)
        if (2 in lst) and (3 in lst) or (5 in lst):
            return True
        else:
            return False

    # sprawdza czy jest kareta
    def check_carriage(self, lst):
        lst = self.numbers_counter_list(lst)
        if [i for i in lst if i >= 4]:
            return True
        else:
            return False

    # sprawdza czy jest poker
    def check_poker(self, lst):
        lst = self.numbers_counter_list(lst)
        if 5 in lst:
            return True
        else:
            return False

    # zwraca listę par
    def one_pair_list(self, lst):
        list_pair = []
        lst = self.numbers_counter_list(lst)
        for i, j in enumerate(lst, 1):
            if j >= 2:
                list_pair.append(i)
        return list_pair

    # zwraca listę sum par
    def sum_one_pair_list(self, lst):
        lst = self.one_pair_list(lst)
        x = []
        for n in range(0, len(lst)):
            x.append(lst[n] * 2)
        return x

    # zwraca max z listy par
    def max_sum_one_pair_list(self, lst):
        sum_lst = self.sum_one_pair_list(lst)
        if len(sum_lst) != 0:
            lst_max = sum_lst[0]
        else:
            lst_max = 0
        for i in range(0, len(sum_lst)):
            if sum_lst[i] > lst_max:
                lst_max = sum_lst[i]
        return lst_max

    # sumuje kości dwóch par
    def sum_two_pairs(self, lst):
        lst = self.numbers_counter_list(lst)
        value = 0
        for i, j in enumerate(lst, 1):
            if j == 2 and lst.count(3) == 1 or j == 2 and lst.count(2) == 2 or j == 3 and lst.count(2) == 1:
                value += i * 2
            if j >= 4:
                value += i * 4
        return value

    # sumuje kości małego strita
    def sum_small_straight(self, lst):
        if self.check_small_straight(lst):
            lst = self.numbers_counter_list(lst)
            return sum([i for i, j in enumerate(lst, 1) if j == 1])
        else:
            return 0

    # sumuje kości dużego strita
    def sum_big_straight(self, lst):
        if self.check_big_straight(lst):
            lst = self.numbers_counter_list(lst)
            return sum([i for i, j in enumerate(lst, 1) if j == 1])
        else:
            return 0

    # sumuje kości trójki
    def sum_three(self, lst):
        lst = self.numbers_counter_list(lst)
        if 3 in lst:
            return sum([i * j for i, j in enumerate(lst, 1) if j == 3])
        if 4 in lst:
            return sum([i * (j - 1) for i, j in enumerate(lst, 1) if j == 4])
        if 5 in lst:
            return sum([i * (j - 2) for i, j in enumerate(lst, 1) if j == 5])
        if 3 or 4 or 5 not in lst:
            return 0

    # sumuje kości pokera
    def sum_full(self, lst):
        lst = self.numbers_counter_list(lst)
        value = 0
        for i, j in enumerate(lst, 1):
            if lst.count(2) == 1 and lst.count(3) == 1 or lst.count(5) == 1:
                value += i * j
        return value

    # sumuje kości karety
    def sum_carriage(self, lst):
        lst = self.numbers_counter_list(lst)
        if 4 in lst:
            value = sum([i * j for i, j in enumerate(lst, 1) if j == 4])
        else:
            value = sum([i * (j - 1) for i, j in enumerate(lst, 1) if j == 5])
        return value

    # sumuje kości pokera
    def sum_poker(self, lst):
        lst = self.numbers_counter_list(lst)
        return sum([i * j for i, j in enumerate(lst, 1) if j == 5])

    # sumuje wszystkie kości
    def sum_all_elements(self, lst):
        return sum([i for i in lst])


    def score_report(self, lst):
        print('[1] Jedynka   ', self.check_number(1, lst), '\t\t-> ', self.quantity_numbers(1, lst))
        print('[2] Dwójka    ', self.check_number(2, lst), '\t\t-> ', self.quantity_numbers(2, lst) * 2)
        print('[3] Trójka    ', self.check_number(3, lst), '\t\t-> ', self.quantity_numbers(3, lst) * 3)
        print('[4] Czwórka   ', self.check_number(4, lst), '\t\t-> ', self.quantity_numbers(4, lst) * 4)
        print('[5] Piątka    ', self.check_number(5, lst), '\t\t-> ', self.quantity_numbers(5, lst) * 5)
        print('[6] Szóstka   ', self.check_number(6, lst), '\t\t-> ', self.quantity_numbers(6, lst) * 6)
        print('')
        print('    B O N U S', Score.bonus(lst))
        print('')
        print('[A] Para      ', self.check_one_pair(lst), ' \t\t-> ', self.one_pair_list(lst), ' -> ',
              self.sum_one_pair_list(lst), ' -> ', self.max_sum_one_pair_list(lst))
        print('[B] Dwie Pary ', self.check_two_pairs(lst), '\t\t-> ', self.sum_two_pairs(lst))
        print('[C] Mały strit', self.check_small_straight(lst), '\t\t-> ', self.sum_small_straight(lst))
        print('[D] Duży strit', self.check_big_straight(lst), '\t\t-> ', self.sum_big_straight(lst))
        print('[E] Trójka    ', self.check_three(lst), '\t\t-> ', self.sum_three(lst))
        print('[F] Ful       ', self.check_full(lst), '\t\t-> ', self.sum_full(lst))
        print('[G] Kareta    ', self.check_carriage(lst), '\t\t-> ', self.sum_carriage(lst))
        print('[H] Poker     ', self.check_poker(lst), '\t\t-> ', self.sum_poker(lst))
        print('[I] Szansa    ', self.check_chance(lst), '\t\t-> ', self.sum_all_elements(lst))


