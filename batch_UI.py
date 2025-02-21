__author__ = "Dorian Bansoodeb"


# All imports of required files
import sort
import load_data
import curve_fit
import histogram

# Asks the user to give the file with the commands
user_file = input(
    "Please enter the name of the file where your commands are stored:")

# Opens the inputted file
user_commands = open(user_file, "r")


# Runs through each command line
for line in user_commands:
    # Cleans the lines and separates the variables
    line = line.strip().split(';')

    # L)oad Data
    if line[0] == 'L' or line[0] == 'l':
        file_name = line[1]
        attribute = line[2]
        att_value = line[3]
        data_set = load_data.calculate_health(load_data.load_data(file_name, (attribute,
                                                                              att_value)))
        print("Data loaded")

    # S)ort Data
    elif line[0] == 'S' or line[0] == 's':
        attribute = line[1]
        order = line[2]
        show = line[3]
        sorted_data = sort.sort(data_set, order, attribute)
        if show == 'Y':  # If user wants to see sorted data
            print(sorted_data)

    # C)urve Fit
    elif line[0] == 'C' or line[0] == 'c':
        attribute = line[1]
        integer = line[2]
        curvefit_data = curve_fit.curve_fit(data_set, attribute, integer)

    # H)istogram
    elif line[0] == 'H' or line[0] == 'h':
        attribute = line[1]
        histogram_data = histogram.histogram(data_set, attribute)

    # E)xit
    elif line[0] == 'E' or line[0] == 'e':
        print("Exiting program.../nGood-bye!")

