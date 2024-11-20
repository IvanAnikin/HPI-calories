# -*- coding: utf-8 -*-
"""Copy of Kcal_tracker.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16_8tWc9B1_Z5aSG65mgqYuadLjQAuIxc
"""

# MIT License
#
# Copyright (c) 2024 The Incredible 4
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


def kcal(weight, height, genre, sport, age):
    if genre == "man" or genre == "Man" and sport == 1:
        energy = (66 + (13.7 * weight)) + ((5 * height) - (6.8 * age)) * 1.2

    elif genre == "man" or genre == "Man" and sport == 2:
        energy = (66 + (13.7 * weight)) + ((5 * height) - (6.8 * age)) * 1.375

    elif genre == "man" or genre == "Man" and sport == 3:
        energy = (66 + (13.7 * weight)) + ((5 * height) - (6.8 * age)) * 1.55

    elif genre == "man" or genre == "Man" and sport == 4:
        energy = (66 + (13.7 * weight)) + ((5 * height) - (6.8 * age)) * 1.725

    elif genre == "man" or genre == "Man" and sport == 5:
        energy = (66 + (13.7 * weight)) + ((5 * height) - (6.8 * age)) * 1.9

    elif genre == "woman" or genre == "Woman" and sport == 1:
        energy = (665 + (9.6 * weight)) + ((1.8 * height) - (4.7 * age)) * 1.2

    elif genre == "woman" or genre == "Woman" and sport == 2:
        energy = (665 + (9.6 * weight)) + ((1.8 * height) - (4.7 * age)) * 1.375

    elif genre == "woman" or genre == "Woman" and sport == 3:
        energy = (665 + (9.6 * weight)) + ((1.8 * height) - (4.7 * age)) * 1.55

    elif genre == "woman" or genre == "Woman" and sport == 4:
        energy = (665 + (9.6 * weight)) + ((1.8 * height) - (4.7 * age)) * 1.725

    elif genre == "woman" or genre == "Woman" and sport == 5:
        energy = (665 + (9.6 * weight)) + ((1.8 * height) - (4.7 * age)) * 1.9
    return energy



def kcal_calc(food, kcal):
    energy_values = [("Tuna", 130), ("French_fries", 312), ("Meatballs", 200),
                      ("Beef", 250), ("Fried_chicken", 246), ("Rice", 130), ("Hamburguer", 300),
                        ("Pizza", 320), ("Pasta", 158), ("Boiled_eggs", 155), ("Tortilla", 160),
                          ("Hot_dogs", 400), ("Salad", 89), ("Sausages", 300), ("Taco", 226), ("Cake", 372),
                            ("Watermelon", 36), ("Croquetas", 110), ("Croissant", 406), ("Avocado", 140), ("Meat", 175)]
    kcal_amount = 0
    energy_kcal = kcal(weight, height, genre, sport, age)
    for meal, load in food:
        for food_list, nutricional_value in energy_values:
            if meal == food_list:
                kcal_amount += load * (nutricional_value / 100)
    if kcal_amount < energy_kcal:
        remaining = round(energy_kcal - kcal_amount, 2)
        return f"You have to consume {remaining} kcal more today"
    elif kcal_amount > energy_kcal:
        passed = round(kcal_amount - energy_kcal, 2)
        return f"You passed your daily amount of kcal by {passed}"



if __name__ == "__main__":
    weight = float(input("Enter your weight in kilograms: "))
    height = int(input("Enter your height in centimetres: "))
    genre = ""
    sport = 0
    age = 0
    while age <= 0 or age > 100:
        age = int(input("Enter your age:"))
        if age <= 0 or age > 100:
            print("Your age it's out of range try again please")
    while genre not in ["man", "Man", "woman", "Woman"]:
        genre = str(input("Enter your genre: "))
        if genre not in ["man", "Man", "woman", "Woman"]:
            print("You spelled wrong your genre try again please")
    while sport < 1 or sport > 5:
        sport = int(input("Enter 1 if you are a sedentary person "
                         "\nEnter 2 if you practice sport once to three times a week "
                          "\nEnter 3 if you practice sport three to five times a week"
                           "\nEnter 4 if you practice sport six to seven times a week "
                             "\nEnter 5 if you are a professional athlete:"))
        if sport < 1 or sport > 5:
            print("Your value is out of range try again please")
    basic_kcal = kcal(weight, height, genre, sport, age)
    print("Your daily consumption of kcal is around", round(basic_kcal)gf)
    amount = int(input("How many meals did you take today: "))
    print("we have the following list of food:\n"
    "Tuna, French fries, Meatballs, Beef, Fried Chicken, Rice,  Hamburguer\n"
    "Pizza, Pasta, Boiled eggs, Tortilla, Hot Dogs, Salad, Sausages\n"
    "Taco, Cake, Watermelon, Croquetas, Croissant, Avocado, Meat")
    food = []
    for different_food in range(amount):
        food_quantity = ()
        foods = str(input("Write what you ate(if it's more than two words separe them with an underscore): "))
        quantity = int(input("Write the amount(in grams): "))
        food_quantity = (foods, quantity)
        food.append(food_quantity)
    print(kcal_calc(food, kcal))