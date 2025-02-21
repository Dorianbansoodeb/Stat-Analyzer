__author__ = "Dorian Bansoodeb"

import numpy as np


def curve_fit(chs: list[dict], attribute: str, order: int) -> str:
    """Return the curve of best for the average of health.
    Precondition: 1 <= deg <= 5.
    >>> curve_fit([{'Health': 13, 'Stamina': 2, 'Strength': 24}, {'Health':65, 'Stamina': 69, 'Strength': 17}], 'Stamina', 4)

    '0.776x + 11.448'

    >>> curve_fit([{'Health': 13, 'Stamina': 2, 'Strength': 24}, {'Health':65, 'Stamina': 69, 'Strength': 17}, {'Health': 8, 'Stamina': 4, 'Strength': 3}], 'Strength', 2)

    '-0.548x^2 + 15.0238x + -32.143'

    >>> curve_fit([{'Health': 13, 'Stamina': 2, 'Strength': 24}, {'Health':65, 'Stamina': 69, 'Strength': 17}, {'Health': 8, 'Stamina': 4, 'Strength': 3}, {'Health': 60, 'Stamina': 4, 'Strength': 80},{'Health': 70, 'Stamina': 4, 'Strength': 59}], 'Strength', 5)

    -0.000229x^4 + 0.0372x^3 + -1.864x^2 + 29.723x + -65.378
    """
    health_list = []
    reference_list = []
    for ch in chs:
        health_list.append(ch['Health'])
        reference_list.append(ch[attribute])

    if len(health_list) - 1 < order:
        order = len(health_list) - 1

    line = np.polyfit(reference_list, health_list, order)

    if order == 1:
        return f"{line[0]}x + {line[1]}"
    if order == 2:
        return f'{line[0]}x^2 + {line[1]}x + {line[2]}'
    if order == 3:
        return f'{line[0]}x^3 + {line[1]}x^2 + {line[2]}x + {line[3]}'
    if order == 4:
        return f'{line[0]}x^4 + {line[1]}x^3 + {line[2]}x^2 + {line[3]}x + {line[4]}'
    if order == 5:
        return f'{line[0]}x^5 + {line[1]}x^4 + {line[2]}x^3 + {line[3]}x^2 + {line[4]}x + {line[5]}'


