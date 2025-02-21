__author__ = "Dorian Bansoodeb"


def sort_characters_agility_bubble(chs: list[dict], order: str) -> list[dict]:
    """Return the charecters given in ascending or discending order based on their agility.
    Precondition: order == 'A' or order == 'D'
    >>> sort_characters_agility_bubble([{'Occupation': 'EB', 'Agility': 13},
    {'Occupation': 'H', 'Agility': 11}], 'A')

    [{'Occupation': 'H', 'Agility': 11}, {'Occupation': 'EB','Agility': 13}]

    >>> sort_characters_agility_bubble([{'Occupation':'EB'},
    {'Occupation': 'M'}], 'D')

    "Agility" key is not present.
    [{'Occupation': 'EB'},{'Occupation': 'M'}]

    >>> sort_characters_agility_bubble([{'Agility': 13}], 'D')

    [{'Agility': 13}]
    """
    swap = True
    for ch in chs:
        if 'Agility' not in ch:
            print('"Agility" key is not present')
            return chs

    if order == 'A':
        while swap:
            swap = False
            for i in range(len(chs) - 1):
                if chs[i]['Agility'] > chs[i + 1]['Agility']:
                    aux = chs[i]
                    chs[i] = chs[i + 1]
                    chs[i + 1] = aux
                    swap = True

        return chs

    if order == 'D':
        while swap:
            swap = False
            for i in range(len(chs) - 1):
                if chs[i]['Agility'] < chs[i + 1]['Agility']:
                    aux = chs[i]
                    chs[i] = chs[i + 1]
                    chs[i + 1] = aux
                    swap = True
        return chs


def sort_characters_intelligence_selection(characters: list[dict], asc_or_des: str) -> (list[dict]):
    """
    Return a sorted list given a list of dictionnaries, and the order to sort it in (Ascending or Descending)
    Preconditions: asc_or_des is either "A" or "D", and a list of dictionnaries is included

    >>>sort_characters_intelligence_selection([{'Occupation': 'EB','Intelligence': 9}, {'Occupation': 'H','Intelligence': 12}], "D")
    [{'Occupation': 'H', 'Intelligence': 12}, {'Occupation': 'EB','Intelligence': 9}]

    >>>sort_characters_intelligence_selection([{'Occupation':'EB'},{'Occupation': 'M'}], "D")
    "Intelligence" key is not present
    [{'Occupation': 'EB'}, {'Occupation': 'M'}]

    >>>sort_characters_intelligence_selection([{'Occupation': 'AT', 'Strength': 13, 'Agility': 2, 'Stamina': 6, 
    'Personality': 7, 'Intelligence': 12, 'Luck': 0.67, 'Armor': 8}, 
    {'Occupation': 'AT', 'Strength': 12, 'Agility': 3, 'Stamina': 7, 
    'Personality': 13, 'Intelligence': 11, 'Luck': 0.33, 'Armor': 8},
    {'Occupation': 'AT', 'Strength': 9, 'Agility': 9, 'Stamina': 8, 
    'Personality': 8, 'Intelligence': 5, 'Luck': 0.72, 'Armor': 10}],"A")

    [{'Occupation': 'AT', 'Strength': 9, 'Agility': 9, 'Stamina': 8, 
    'Personality': 8, 'Intelligence': 5, 'Luck': 0.72, 'Armor': 10}, 
    {'Occupation': 'AT', 'Strength': 12, 'Agility': 3, 'Stamina': 7, 
    'Personality': 13, 'Intelligence': 11, 'Luck': 0.33, 'Armor': 8}, 
    {'Occupation': 'AT', 'Strength': 13, 'Agility': 2, 'Stamina': 6, 
    'Personality': 7, 'Intelligence': 12, 'Luck': 0.67, 'Armor': 8}]

    """
    intel = False
    for character in characters:
        if intel == False:
            intelligence = character.get('Intelligence')
            if intelligence != None:
                intel = True

    if intel == False:
        print('"Intelligence" key is not present')
        return characters
    if (asc_or_des == "A"):
        for i in range(len(characters)):
            min_idx = i

            for j in range(i + 1, len(characters)):
                if characters[min_idx]["Intelligence"] > characters[j]["Intelligence"]:
                    min_idx = j

            characters[i], characters[min_idx] = characters[min_idx], characters[i]

    elif (asc_or_des == "D"):
        for i in range(len(characters)):
            max_idx = i

            for j in range(i + 1, len(characters)):
                if characters[max_idx]["Intelligence"] < characters[j]["Intelligence"]:
                    max_idx = j

            characters[i], characters[max_idx] = characters[max_idx], characters[i]

    else:
        return

    return characters


def sort_characters_health_insertion(arr: list[dict], order: str) -> (list[dict]):
    """
    Sorts a list of dictionaries with character information by their 'Health' attribute in either ascending or descending order via insertion sort algorithm.

    Preconditions: order = 'A' or 'D'

    Returns sorted list of dictionairies by ascending or descending health, or a string stating health attribute is not present (if that is the case).

    >>>sort_characters_health_insertion([{'Occupation': 'EB','Health': 62.37}, {'Occupation': 'H', 'Health': 62.71}], 'A')
    [{'Occupation': 'EB', 'Health': 62.37}, {'Occupation': 'H', 'Health': 62.71}]

    >>>sort_characters_health_insertion([{'Occupation': 'H', 'Health': 100.034}, {'Occupation': 'EB', 'Health': 2.340}, {'Occupation': 'H', 'Health': 52.003}], "D")
    [{'Occupation': 'H', 'Health': 100.034}, {'Occupation': 'H', 'Health': 52.003}, {'Occupation': 'EB', 'Health': 2.34}]

    >>>sort_characters_health_insertion([{'Occupation': 'P'}, {'Occupation': 'M'}], "D")
    There is no Health in this List!
    [{'Occupation': 'P'}, {'Occupation': 'M'}]

    >>>sort_characters_health_insertion([{'Occupation': 'EB','Health': 62.37}, {'Occupation': 'H', 'Health': 62.71}], "Q")
    'Please specify if Health should be arranged Ascending or Descending via A or D!'
    """
    health_in_list = False
    for char in arr:
        if "Health" in char:
            health_in_list = True
    if health_in_list == False:
        print('"Health" key is not present!')
    if health_in_list == True:
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1

            if order == 'A':
                while j >= 0 and arr[j]['Health'] > key['Health']:
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = key

            elif order == 'D':
                while j >= 0 and arr[j]['Health'] < key['Health']:
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = key

            else:
                print(
                    "Please specify if Health should be arranged Ascending or Descending via A or D!")
    return arr


def sort_characters_armor_bubble(character_list: list[dict], order: str) -> list:
    """Return a sorted character list either in ascending or descending order,
    given a chracter_list and a specified order.
    Preconditions: 'character_list' must be an iterable object and 'order' must be 'A' or 'D'

    >>>sort_characters_armor_bubble([{'Occupation': 'EB', 'Armor': 11}, 
    {'Occupation': 'H', 'Armor': 10}], "D")
    [{'Occupation': 'EB', 'Armor': 11}, {'Occupation': 'H', 'Armor': 10}]

    >>>sort_characters_armor_bubble([{'Occupation': 'EB'}, {'Occupation': 'M'}], "D")
    "Armor" key is not present.
    [{'Occupation': 'EB'}, {'Occupation': 'M'}]

    """

    swap = True

    # If user chooses Ascending order:
    if order == 'A':
        while swap:
            swap = False
            for i in range(len(character_list) - 1):
                try:
                    character_list[i]['Armor']
                except:
                    print("Armor is missing from the dictionaries.")
                    return character_list
                else:
                    if character_list[i]['Armor'] > character_list[i + 1]['Armor']:
                        hold = character_list[i]
                        character_list[i] = character_list[i + 1]
                        character_list[i + 1] = hold
                        """character_list[i]['Armor'], character_list[i +
                                                                   1]['Armor'] = character_list[i + 1]['Armor'], character_list[i]['Armor']"""
                        swap = True

    # If user chooses Descending order:
    elif order == 'D':
        while swap:
            swap = False
            for i in range(len(character_list) - 1):
                try:
                    character_list[i]['Armor']
                except:
                    print('Armor is not present in one of the dictionaries.')
                    return character_list
                else:
                    if character_list[i]['Armor'] < character_list[i + 1]['Armor']:
                        hold = character_list[i]
                        character_list[i] = character_list[i + 1]
                        character_list[i + 1] = hold
                        """character_list[i]['Armor'], character_list[i +
                                                                   1]['Armor'] = character_list[i + 1]['Armor'], character_list[i]['Armor']"""
                        swap = True
    else:
        print('Invalid order input')
    return character_list


def sort(characters: list[dict], asc_or_des: str, attribute: str):
    """
    Return the sorted character list in ascending or descending order given the
    specific attribute and order to sort by. 

    Precondition: asc_or_des has to be "A" or "D", character list must be a list
    and must be one of the four attributes

   >>>sort([{'Occupation': 'EB', 'Armor': 11}, {'Occupation': 'H', 'Armor': 10}], "A","Armor") 
   [{'Occupation': 'H', 'Armor': 10}, {'Occupation': 'EB', 'Armor': 11}]

   >>>sort([{'Occupation': 'EB', 'Armor': 11}, {'Occupation': 'H', 'Armor': 10}], "A","aojsnfwbof")
   Cannot be sorted by aojsnfwbof
   [{'Occupation': 'EB', 'Armor': 11}, {'Occupation': 'H', 'Armor': 10}]

   >>>sort([{'Occupation': 'EB', 'Agility': 13}, {'Occupation': 'H', 'Agility': 11}], "D", "Agility")
   [{'Occupation': 'EB', 'Agility': 13}, {'Occupation': 'H', 'Agility': 11}]


    """

    if attribute == "Agility":
        return sort_characters_agility_bubble(characters, asc_or_des)

    if attribute == "Intelligence":
        return sort_characters_intelligence_selection(characters, asc_or_des)

    if attribute == "Health":
        return sort_characters_health_insertion(characters, asc_or_des)

    if attribute == "Armor":
        return sort_characters_armor_bubble(characters, asc_or_des)

    print(f"Cannot be sorted by {attribute}")
    return characters


