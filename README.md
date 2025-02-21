Dorian Bansoodeb

This application allows users to load, sort, analyze, and visualize data through a text-based user interface (text_UI) or batch processing (batch_UI). The system supports commands for loading data, sorting it, fitting a curve, generating a histogram, and exiting the application.

Requirements

Python 3.x

Required libraries: numpy, matplotlib

Ensure the following modules are present in the working directory:

load_data.py

sort.py

histogram.py

curve_fit.py

Running the Application

1. Using Text-Based User Interface (text_UI)

The text_UI.py script allows users to interact with the application by entering commands manually.

How to Run:

python text_UI.py

Available Commands:

L (Load Data): Load data from a file based on a chosen attribute.

S (Sort Data): Sorts the data by a selected attribute.

C (Curve Fit): Fits a polynomial curve to the data.

H (Histogram): Generates a histogram for a specified attribute.

E (Exit): Closes the application.

Example Workflow:

Load data: L

Enter file name and attribute to filter.

Sort data: S

Select sorting attribute and order (Ascending/Descending).

Generate histogram: H

Exit the program: E

2. Using Batch Processing (batch_UI)

The batch_UI.py script processes commands from a file, executing them in sequence.

How to Run:

python batch_UI.py

Instructions:

Prepare a text file containing commands, with each line formatted as:

Command;Parameter1;Parameter2;Parameter3;...

Example command file:

L;data.csv;Strength;10-50
S;Health;A;Y
C;Agility;2
H;Armor
E

When prompted, enter the name of your command file.

The application will process each command sequentially.

Notes

Ensure that the dataset file is available and correctly formatted.

The program does not support using 'All' as an attribute when filtering data.

Invalid inputs will prompt the user to re-enter values.

Troubleshooting

If an error occurs while loading data, verify that the file path and attribute names are correct.

Ensure that required dependencies (numpy, matplotlib) are installed.

Check that batch command files follow the correct format.
