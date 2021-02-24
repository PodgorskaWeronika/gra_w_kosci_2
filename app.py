from flask import Flask, request
from flask import render_template
from dice_class import *

app = Flask(__name__)

players = 4

data_1 = {"Jedynki": 1, "Dwójki": 2, "Trójki": 3, "Czwórki": 4, "Piątki": 5, "Szóstki": 6, "BONUS": 0,
          "Jedna para": 10, "Dwie pary": 12, "Mały strit": 15, "Duży strit": 20, "Trójka": 18,
          "Full": 19, "Kareta": 16, "Poker": 50, "Szansa": 22, "SUMA": 1000}

data_2 = {"Jedynki": 3, "Dwójki": 6, "Trójki": 9, "Czwórki": 12, "Piątki": 15, "Szóstki": 18, "BONUS": 35,
          "Jedna para": 4, "Dwie pary": 10, "Mały strit": 0, "Duży strit": 40, "Trójka": 9,
          "Full": 20, "Kareta": 24, "Poker": 0, "Szansa": 30, "SUMA": 2000}

data_3 = {"Jedynki": 4, "Dwójki": 8, "Trójki": 12, "Czwórki": 16, "Piątki": 20, "Szóstki": 24, "BONUS": 35,
          "Jedna para": 12, "Dwie pary": 24, "Mały strit": 30, "Duży strit": 0, "Trójka": 15,
          "Full": 8, "Kareta": 24, "Poker": 50, "Szansa": 22, "SUMA": 3000}

data_4 = {"Jedynki": 1, "Dwójki": 2, "Trójki": 3, "Czwórki": 4, "Piątki": 5, "Szóstki": 6, "BONUS": 35,
          "Jedna para": 10, "Dwie pary": 12, "Mały strit": 15, "Duży strit": 20, "Trójka": 18,
          "Full": 19, "Kareta": 16, "Poker": 50, "Szansa": 22, "SUMA": 1000}

values = [data_1, data_2, data_3, data_4]

dice = Dice()



def change_list(lst):
    return [int(x) for x in lst]

numbers = dice.many_dice_roll()

@app.route('/', methods=['GET', 'POST'])
def score():

    print("pierwsze losowanie", numbers)
    if request.method == "POST":
        lst = request.form.getlist('mycheckbox')
        numbers_to_change = change_list(lst)
        print("Numery kostek do zmiany", numbers_to_change)
        next_numbers = dice.selected_dice_roll(numbers, numbers_to_change)
        print("ponowne losowanie", next_numbers)
        return render_template('index.html', players=players, numbers=next_numbers, scores=values)
    return render_template('index.html', players=players, numbers=numbers, scores=values)


if __name__ == '__main__':
    app.run(debug=True)
