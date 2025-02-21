__author__ = "Dorian Bansoodeb"

import numpy as np
import matplotlib.pyplot as plt


def histogram(characters, attribute):
    """
    Graph a histogram using a list of character dictionaries, and the attribute selected

    preconditions: A list containing dictionaries of characters, and the 
    attribute provided in in the prompt is present in the list of dictionaries of characters

    histogram([{'Occupation': 'AT', 'Strength': 9, 'Agility': 9, 'Stamina': 8,
         'Personality': 8, 'Intelligence': 5, 'Luck': 0.72, 'Armor': 10},
        {'Occupation': 'A', 'Strength': 12, 'Agility': 3, 'Stamina': 7,
         'Personality': 13, 'Intelligence': 11, 'Luck': 0.33, 'Armor': 8},
        {'Occupation': 'B', 'Strength': 18, 'Agility': 2, 'Stamina': 6,
         'Personality': 7, 'Intelligence': 12, 'Luck': 0.67, 'Armor': 8},
        {'Occupation': 'AT', 'Strength': 9, 'Agility': 9, 'Stamina': 8,
         'Personality': 8, 'Intelligence': 18, 'Luck': 0.72, 'Armor': 10},
        {'Occupation': 'A', 'Strength': 12, 'Agility': 3, 'Stamina': 7,
         'Personality': 13, 'Intelligence': 5, 'Luck': 0.33, 'Armor': 8},
        {'Occupation': 'B', 'Strength': 18, 'Agility': 2, 'Stamina': 6,
         'Personality': 7, 'Intelligence': 1, 'Luck': 0.67, 'Armor': 8}],"Intelligence")

    >>>18

    histogram([{'Occupation': 'B', 'Strength': 18, 'Agility': 2, 'Stamina': 6,
         'Personality': 7, 'Intelligence': 12, 'Luck': 0.67, 'Armor': 8},
        {'Occupation': 'AT', 'Strength': 9, 'Agility': 9, 'Stamina': 8,
         'Personality': 8, 'Intelligence': 18, 'Luck': 0.72, 'Armor': 10},
        {'Occupation': 'A', 'Strength': 12, 'Agility': 3, 'Stamina': 7,
         'Personality': 13, 'Intelligence': 5, 'Luck': 0.33, 'Armor': 8}],"Occupation")
    >>>-1

    histogram([{'Occupation': 'AT', 'Strength': 9, 'Agility': 9, 'Stamina': 8,
         'Personality': 8, 'Intelligence': 5, 'Luck': 0.72, 'Armor': 10},
        {'Occupation': 'A', 'Strength': 12, 'Agility': 3, 'Stamina': 7,
         'Personality': 13, 'Intelligence': 11, 'Luck': 0.33, 'Armor': 8},
        {'Occupation': 'B', 'Strength': 18, 'Agility': 2, 'Stamina': 6,
         'Personality': 7, 'Intelligence': 12, 'Luck': 0.67, 'Armor': 8},
        {'Occupation': 'AT', 'Strength': 9, 'Agility': 9, 'Stamina': 8,
         'Personality': 8, 'Intelligence': 18, 'Luck': 0.72, 'Armor': 10},
        {'Occupation': 'A', 'Strength': 12, 'Agility': 3, 'Stamina': 7,
         'Personality': 13, 'Intelligence': 5, 'Luck': 0.33, 'Armor': 8},
        {'Occupation': 'B', 'Strength': 18, 'Agility': 2, 'Stamina': 6,
         'Personality': 7, 'Intelligence': 1, 'Luck': 0.67, 'Armor': 8}],"Luck")
    >>>0.72





    """

    if isinstance(characters[0][attribute], str):
        unique_str = set()
        unique_y = []
        unique_list = []
        for character in characters:
            if character[attribute] not in unique_str:
                unique_str.add(character[attribute])

        for unique in unique_str:
            unique_y.append(0)
            unique_list.append(unique)

        for i in range(len(unique_list)):
            for character in characters:
                if character[attribute] == unique_list[i]:
                    unique_y[i] += 1

        fig1 = plt.figure()
        plt.title(attribute)
        plt.xlabel("x-values")
        plt.ylabel("Frequency")
        plt.bar(unique_list, unique_y)
        plt.show()
        return -1

    else:

        values = []
        for character in characters:
            values.append(character[attribute])

        interval = (max(values) / 20)
        interval_y = [0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        intervals = []
        for i in range(20):
            intervals.append(0 + i * interval)

        for i in range(20):
            for value in values:
                if i == 0 and value < intervals[1]:
                    interval_y[i] += 1
                elif i == 19 and value >= intervals[19]:
                    interval_y[i] += 1
                elif value >= intervals[i] and value < intervals[i + 1]:
                    interval_y[i] += 1

        fig1 = plt.figure()
        plt.bar(intervals, interval_y)
        plt.xticks(intervals)
        plt.title(attribute)
        plt.xlabel("x-values")
        plt.ylabel("Frequency")
        plt.show()
        return max(values)



