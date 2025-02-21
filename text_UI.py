__author__ = "Dorian Bansoodeb"

# Importing

from load_data import load_data
from load_data import calculate_health
from sort import sort
from histogram import histogram
from curve_fit import curve_fit
import numpy as np
import matplotlib.pyplot as plt

list_of_supported_operators = [
    "L", "l", "S", "s", "C", "c", "H", "h", "E", "e"]


def execute_textUI():
    """
    Executes a text-based user interface for interacting with data.

    Supported commands:
         -L or l for Load Data: loading data from a file
         -S or s for Sort Data: sorting the data from the loaded file
         -C or c for Curve Fit: fitting a curve
         -H or h for Histogram: plotting
         -E or e for Exit: exiting the program
    """

    loaded_data = None  # Initialize loaded data
    user_interface = """The available commands are:
              L)oad Data
              S)ort Data
              C)urve Fit
              H)istogram
              E)xit
        Please type your command: """
    executed_command = input(user_interface)

    while len(executed_command) != 1 or executed_command not in list_of_supported_operators:
        print("Invalid command.")
        executed_command = input(user_interface)

    while executed_command in list_of_supported_operators[0:8]:

        # Load Data:
        if executed_command in list_of_supported_operators[0:2]:
            file_name = input("Please enter the name of the file: ")
            attribute = input(
                "Please enter the attribute to use as a filter: ")
            while attribute == 'All':
                attribute = input(
                    "'All' cannot be an attribute. Please enter a valid attribute to use as a filter: ")
            if attribute != 'All':
                if attribute == 'Strength':
                    min_value = int(input(
                        "Please enter the minimum value of the attribute: "))
                    max_value = int(input(
                        "Please enter the maximum value of the attribute: "))
                    loaded_data_a = load_data(
                        file_name, (attribute, (min_value, max_value)))
                    for entry in loaded_data_a:
                        entry["Strength"] = entry[attribute]
                    loaded_data = calculate_health(loaded_data_a)

                if attribute == 'Luck':
                    value = input(
                        "please enter the value of the attribute: ")
                    luck_value = float(value)
                    loaded_data_b = load_data(
                        file_name, (attribute, luck_value))
                    for entry in loaded_data_b:
                        entry["Luck"] = luck_value
                    loaded_data = calculate_health(loaded_data_b)

                if attribute != 'Strength' and attribute != 'Luck':
                    value = input(
                        "Please enter the value of the attribute: ")
                    loaded_data_b = load_data(file_name, (attribute, value))
                    loaded_data = calculate_health(loaded_data_b)

                if loaded_data:
                    print("Data loaded")
                else:
                    print("Inavalid command or failed to load data")
                executed_command = input(user_interface)

        # Sort Data:
        elif executed_command in list_of_supported_operators[2:4]:
            if not loaded_data:
                print("File not loaded. Please load a file first.")
            elif loaded_data:
                attribute = input(
                    "Please enter the attribute you want to use for sorting: 'Agility', 'Armor', 'Intelligence', 'Health': ")
                order = input("Ascending (A) or Descending (D) order: ")
                sorted_data = sort(loaded_data, order, attribute)
                if sorted_data:
                    display_option = input(
                        "Data Sorted. Do you want to display the data? (Y/N): ")
                    if display_option == 'Y':
                        print(sorted_data)
                    if display_option == 'N':
                        print("Sort data not displayed")
                else:
                    print("Invalid command or failed to sort data")
            executed_command = input(user_interface)

        # Curve Fit:
        elif executed_command in list_of_supported_operators[4:6]:
            if not loaded_data:
                print("File not loaded. Please load a file first.")
            elif loaded_data:
                attribute = input(
                    "Please enter the attribute you want to use to find the best fit for Health: ")
                order = int(
                    input("Please enter the order of the polynomial to be fitted: "))
                curve_equation = curve_fit(loaded_data, attribute, order)
                if curve_equation:
                    print("Curve fitted successfully.")
                    print("Equation of the curve fit:", curve_equation)
                else:
                    print("Failed to perform curve fitting.")
                    int_order = int(order)
            executed_command = input(user_interface)

        # Histogram:
        elif executed_command in list_of_supported_operators[6:8]:
            if not loaded_data:
                print("File not loaded. Please load a file first.")
            if loaded_data:
                attribute = input(
                    "Please enter the attribute you want to use for plotting: ")
                histogram(loaded_data, attribute)
            executed_command = input(user_interface)
    if executed_command in list_of_supported_operators[8:10]:
        print("Exiting program.")
        return


# Execute the text UI
if __name__ == '__main__':
    execute_textUI()

