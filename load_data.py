__author__ = "Dorian Bansoodeb"


def character_occupation_list(file_name: str, occupation: str) -> list[dict]:
    """Return a list of all the charecters with the given occupation in a file.
    >>> character_occupation_list('characters-mat.csv', 'AT')
    [{'Strength': 13, 'Agility': 2, 'Stamina': 6, 'Personality': 7,
    'Intelligence': 8, 'Luck': 0.67, 'Armor': 8, 'Weapon': 'Staff'},
    {another element},
    ...
    ]
    >>> charecter_occupation_list('charecters-mat.csv', 'XXXX')
    []
    """

    file = open(file_name, 'r')
    target_charecters = []
    first_line = True

    for line in file:
        line = line.strip()
        line = line.split(',')
        if first_line:
            header = line
            first_line = False
        else:
            charecter_stats = {}
            charecter_stats[header[0]] = line[0]
            charecter_stats[header[1]] = int(line[1])
            charecter_stats[header[2]] = int(line[2])
            charecter_stats[header[3]] = int(line[3])
            charecter_stats[header[4]] = int(line[4])
            charecter_stats[header[5]] = int(line[5])
            charecter_stats[header[6]] = float(line[6])
            charecter_stats[header[7]] = int(line[7])
            charecter_stats[header[8]] = line[8]

            if charecter_stats['Occupation'] == occupation:
                del charecter_stats['Occupation']
                target_charecters.append(charecter_stats)

    return target_charecters


def character_strength_list(file_name: str, min_and_max: tuple[int]) -> list[dict]:
    """
    Return a list of characters whose strenght falls between the minimum and maximum
    values inclusive.

    >>> character_strength_list ('characters-mat.csv', (11, 13))
    [{'Occupation': 'AT', 'Agility': 2, 'Stamina': 6, 'Personality': 7, 
    'Intelligence': 8, 'Luck': 0.67, 'Armor': 8, 'Weapon': 'Staff'}
    {'Occupation': 'AT', 'Agility': 3, 'Stamina': 7, 'Personality': 13, 
    'Intelligence': 11, 'Luck': 0.33, 'Armor': 8, 'Weapon': 'Staff'}
    {'Occupation': 'AT', 'Agility': 8, 'Stamina': 8, 'Personality': 14, 
    'Intelligence': 11, 'Luck': 0.61, 'Armor': 10, 'Weapon': 'Club'}
    ...
    ]
    >>> character_strength_list ('characters-mat.csv', (10000, 999999))
    []

    >>> character_strength_list ('characters-mat.csv', (0, 10)) 
    [{'Occupation': 'AT', 'Agility': 9, 'Stamina': 8, 'Personality': 8, 
    'Intelligence': 15, 'Luck': 0.72, 'Armor': 10, 'Weapon': 'Staff'}
    {'Occupation': 'AT', 'Agility': 9, 'Stamina': 3, 'Personality': 9, 
    'Intelligence': 15, 'Luck': 0.5, 'Armor': 10, 'Weapon': 'Club'}
    {'Occupation': 'AT', 'Agility': 5, 'Stamina': 9, 'Personality': 12, 
    'Intelligence': 14, 'Luck': 0.78, 'Armor': 9, 'Weapon': 'Dagger'}
    ...
    ]

    """
    """

    Return a list of characters whose strenght falls between the minimum and maximum

    values inclusive.



    >>> character_strength_list ('characters-mat.csv', (11, 13))

    [{'Occupation': 'AT', 'Agility': 2, 'Stamina': 6, 'Personality': 7, 

    'Intelligence': 8, 'Luck': 0.67, 'Armor': 8, 'Weapon': 'Staff'}

    {'Occupation': 'AT', 'Agility': 3, 'Stamina': 7, 'Personality': 13, 

    'Intelligence': 11, 'Luck': 0.33, 'Armor': 8, 'Weapon': 'Staff'}

    {'Occupation': 'AT', 'Agility': 8, 'Stamina': 8, 'Personality': 14, 

    'Intelligence': 11, 'Luck': 0.61, 'Armor': 10, 'Weapon': 'Club'}

    ...

    ]

    >>> character_strength_list ('characters-mat.csv', (10000, 999999))

    []



    >>> character_strength_list ('characters-mat.csv', (0, 10)) 

    [{'Occupation': 'AT', 'Agility': 9, 'Stamina': 8, 'Personality': 8, 

    'Intelligence': 15, 'Luck': 0.72, 'Armor': 10, 'Weapon': 'Staff'}

    {'Occupation': 'AT', 'Agility': 9, 'Stamina': 3, 'Personality': 9, 

    'Intelligence': 15, 'Luck': 0.5, 'Armor': 10, 'Weapon': 'Club'}

    {'Occupation': 'AT', 'Agility': 5, 'Stamina': 9, 'Personality': 12, 

    'Intelligence': 14, 'Luck': 0.78, 'Armor': 9, 'Weapon': 'Dagger'}

    ...

    ]



    """

    character_list = []

    with open(file_name, "r") as in_file:

        header = next(in_file).strip().split(',')

        for line in in_file:

            data = line.strip().split(',')

            character = {}

            character[header[0]] = data[0]

            character['Strength'] = int(data[1])

            character[header[2]] = int(data[2])

            character[header[3]] = int(data[3])

            character[header[4]] = int(data[4])

            character[header[5]] = int(data[5])

            character[header[6]] = float(data[6])

            character[header[7]] = int(data[7])

            character[header[8]] = data[8]

            character_list.append(character)

    min_strength, max_strength = min_and_max

    filtered_characters = [

        character for character in character_list if min_strength <= character['Strength'] <= max_strength]

    return filtered_characters


def character_luck_list(name_of_file: str, luck: float) -> list[dict]:
    """ Returns a list of characters, stored as a dictionary, with a luck value less than the value of the luck input parameter.
    Precondition: 0 < luck
    >>>character_luck_list('characters-mat.csv', 0.1)
    []

    >>>character_luck_list('characters-mat.csv', 0.25)
    [{'Occupation': 'AT', 'Strength': 14, 'Agility': 5, 'Stamina': 6, 'Personality': 13, 'Intelligence': 9, 'Armor': '9', 'Weapon': 'Staff'}, {'Occupation': 'DB', 'Strength': 15, 'Agility': 7, 'Stamina': 6, 'Personality': 7, 'Intelligence': 13, 'Armor': '10', 'Weapon': 'Club'}, {'Occupation': 'DB', 'Strength': 16, 'Agility': 10, 'Stamina': 9, 'Personality': 13, 'Intelligence': 6, 'Armor': '10', 'Weapon': 'Club'}, {'Occupation': 'DB', 'Strength': 12, 'Agility': 9, 'Stamina': 5, 'Personality': 7, 'Intelligence': 7, 'Armor': '10', 'Weapon': 'Club'}, {'Occupation': 'H', 'Strength': 16, 'Agility': 12, 'Stamina': 3, 'Personality': 6, 'Intelligence': 15, 'Armor': '11', 'Weapon': 'Dagger'}, {'Occupation': 'HG', 'Strength': 17, 'Agility': 10, 'Stamina': 9, 'Personality': 14, 'Intelligence': 12, 'Armor': '10', 'Weapon': 'Dagger'}, {'Occupation': 'VF', 'Strength': 16, 'Agility': 6, 'Stamina': 3, 'Personality': 8, 'Intelligence': 8, 'Armor': '9', 'Weapon': 'Sling'}, {'Occupation': 'VF', 'Strength': 18, 'Agility': 10, 'Stamina': 9, 'Personality': 13, 'Intelligence': 6, 'Armor': '10', 'Weapon': 'Club'}, {'Occupation': 'VF', 'Strength': 14, 'Agility': 8, 'Stamina': 8, 'Personality': 10, 'Intelligence': 8, 'Armor': '10', 'Weapon': 'Dagger'}, {'Occupation': 'VF', 'Strength': 12, 'Agility': 4, 'Stamina': 2, 'Personality': 14, 'Intelligence': 14, 'Armor': '9', 'Weapon': 'Dagger'}]

    >>>character_luck_list('characters-mat.csv', 0.21)
    [{'Occupation': 'VF', 'Strength': 12, 'Agility': 4, 'Stamina': 2, 'Personality': 14, 'Intelligence': 14, 'Armor': 9, 'Weapon': 'Dagger'}]
    """
    characters = []

    file = open(name_of_file, "r")
    attributes = None
    first_line = True
    for line in file:
        if first_line:
            attributes = line.strip().split(',')
            first_line = False
        else:
            attribute_data = line.strip().split(',')
            # attribute_data[6] refers to the value of the Luck parameter
            if luck > float(attribute_data[6]):
                data = {
                    # Occupation
                    attributes[0]: attribute_data[0],
                    # Strength
                    attributes[1]: int(attribute_data[1]),
                    # Agility
                    attributes[2]: int(attribute_data[2]),
                    # Stamina
                    attributes[3]: int(attribute_data[3]),
                    # Personality
                    attributes[4]: int(attribute_data[4]),
                    # Intelligence
                    attributes[5]: int(attribute_data[5]),
                    # Armor
                    attributes[7]: int(attribute_data[7]),
                    # Weapon
                    attributes[8]: attribute_data[8]
                }
                characters.append(data)
    file.close()
    return characters


def character_weapon_list(file: str, weapon: str) -> list[dict]:
    """Return a list of dictionaries which include attributes of each 
    character from file excluding 'Weapon', given weapon.
    Preconditions: file_name has the following columns
    ['Occupation', 'Strength', 'Agility', 'Stamina', 'Personality', 'Intelligence', 'Luck',
    'Armor', 'Weapon’]

    >>> character_weapon_list ('characters-mat.csv', 'Staff')
    [{'Occupation': 'AT', 'Strength': 13, 'Agility': 2, 'Stamina': 6,
    'Personality': 7, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 8},
    {another element},
    …
    ]
    >>> character_weapon_list ('characters-mat.csv', 'aaa')
    []
    """

    in_file = open(file, "r")  # "characters-mat.csv"
    first_line = True
    character_list = []
    for line in in_file:
        line = line.strip().split(',')
        if first_line:
            first_line = False
            table_header = line
        else:
            if weapon == line[8]:
                attributes = {}
                attributes[table_header[0]] = line[0]
                attributes[table_header[1]] = int(line[1])
                attributes[table_header[2]] = int(line[2])
                attributes[table_header[3]] = int(line[3])
                attributes[table_header[4]] = int(line[4])
                attributes[table_header[5]] = int(line[5])
                attributes[table_header[6]] = float(line[6])
                attributes[table_header[7]] = int(line[7])
                character_list.append(attributes)
    in_file.close()
    return(character_list)


def load_data(file_name: str, pair_of_values):
    """
    Return a list of dictionaries which fits the criteria provided, given an attribute

    >>>load_data ('characters-mat.csv', ('Weapon','Staff'))
    [{'Occupation': 'AT', 'Strength': 13, 'Agility': 2, 'Stamina': 6, 
    'Personality': 7, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 8}, 
    {'Occupation': 'AT', 'Strength': 12, 'Agility': 3, 'Stamina': 7, 
    'Personality': 13, 'Intelligence': 11, 'Luck': 0.33, 'Armor': 8},
    {'Occupation': 'AT', 'Strength': 9, 'Agility': 9, 'Stamina': 8, 
    'Personality': 8, 'Intelligence': 15, 'Luck': 0.72, 'Armor': 10}
    ...
    ]

    >>>load_data ('characters-mat.csv', ('Luck',0.35))
    [{'Occupation': 'AT', 'Strength': 12, 'Agility': 3, 'Stamina': 7,
    'Personality': 13, 'Intelligence': 11, 'Armor': 8, 'Weapon': 'Staff'}, 
    {'Occupation': 'AT', 'Strength': 8, 'Agility': 10, 'Stamina': 11,
    'Personality': 16, 'Intelligence': 8, 'Armor': 10, 'Weapon': 'Dagger'}, 
    {'Occupation': 'AT', 'Strength': 14, 'Agility': 12, 'Stamina': 4,
    'Personality': 12, 'Intelligence': 10, 'Armor': 11, 'Weapon': 'Dagger'}
    ...
    ]

    >>>load_data('characters-mat.csv', ('Occupation','AT'))
    [{'Strength': 13, 'Agility': 2, 'Stamina': 6, 'Personality': 7, 
    'Intelligence': 8, 'Luck': 0.67, 'Armor': 8, 'Weapon': 'Staff'}, 
    {'Strength': 12, 'Agility': 3, 'Stamina': 7, 'Personality': 13, 
    'Intelligence': 11, 'Luck': 0.33, 'Armor': 8, 'Weapon': 'Staff'}, 
    {'Strength': 9, 'Agility': 9, 'Stamina': 8, 'Personality': 8, 
    'Intelligence': 15, 'Luck': 0.72, 'Armor': 10, 'Weapon': 'Staff'}
    ...
    ]


    """
    key, value = pair_of_values
    if key == 'Weapon':
        return character_weapon_list(file_name, value)
    elif key == 'Occupation':
        return character_occupation_list(file_name, value)
    elif key == 'Strength':
        return character_strength_list(file_name, value)
    elif key == 'Luck':
        return character_luck_list(file_name, value)

    character_list = []
    new_character_list = []
    first_line = True
    in_file = open(file_name, "r")

    for data in in_file:
        data = data.strip().split(',')
        if first_line:
            first_line = False
            header = data

        else:
            character = {}
            character[header[0]] = data[0]
            character[header[1]] = int(data[1])
            character[header[2]] = int(data[2])
            character[header[3]] = int(data[3])
            character[header[4]] = int(data[4])
            character[header[5]] = int(data[5])
            character[header[6]] = float(data[6])
            character[header[7]] = int(data[7])
            character[header[8]] = data[8]

            character_list.append(character)

    if key not in header and key != "All":
        print("Invalid Value")
        return new_character_list

    for character in character_list:
        if key == "All":
            return character_list

    return new_character_list


def calculate_health(stats: list[dict]):
    """Return  the list of dictionaries with the charecters health added.
    >>> calculate_health([{'Strength': 13, 'Agility': 2, 'Stamina': 6,
    'Personality': 7, 'Intelligence': 8, 'Luck': 0.67,
    'Armor': 8, 'Weapon': 'Staff'},
    {another element},
    …
    ])

    [{'Strength': 13, 'Agility': 2, 'Stamina': 6, 'Personality': 7,
    'Intelligence': 8, 'Luck': 0.67, 'Armor': 8, 'Weapon': 'Staff',
    'Health': 41.36},
    {another element},
    …
    ]

    >>> calculate_health([{'Strength': 8, 'Agility': 10, 'Stamina': 11,
    'Personality': 16, 'Intelligence': 8, 'Luck': 0.33,
    'Armor': 10, 'Weapon': 'Dagger'}],
    {another element},
    …
    ])

    [{'Strength': 8, 'Agility': 10, 'Stamina': 11,
    'Personality': 16, 'Intelligence': 8, 'Luck': 0.33,
    'Armor': 10, 'Weapon': 'Dagger', 'Health: 86.0}],
    {another element},
    …
    ]
    """

    for i in range(len(stats)):

        strength = stats[i]['Strength']
        agility = stats[i]['Agility']
        stamina = stats[i]['Stamina']
        personality = stats[i]['Personality']
        intelligence = stats[i]['Intelligence']
        armor = stats[i]['Armor']
        luck = stats[i]['Luck']
        health = (strength + agility + stamina + personality
                  + intelligence) + (armor ** 2 * luck)
        stats[i]['Health'] = health

    return stats
