# Super Timeline parser
### (It is still a WIP)

This code performs forensic analysis using the Plaso tool in a Docker container. The script prompts the user to input the path of a file or directory to be analyzed. The input file can be in zip or unziped folder. The program then copies the file to a temporary directory and runs Plaso analysis on it inside a Docker container.

If the user selects to export the Super Timeline as a CSV file, the program prompts the user for the path of the directory where they want to save the file. The program then runs Plaso export inside the Docker container and saves the output CSV file to the specified directory.

## Requirements:

- Docker installation is required to run this program.
- The Docker image for Plaso is required to run this program. the image can be downloaded using ``` docker pull log2timeline/plaso.```
- The requirements.txt file contains the required Python packages. The packages can be installed using ``` pip install -r requirements.txt```

## Functionality:

The program prompts the user to enter the path of a file or directory to be analyzed.
The input file can be in zip or tar format. If it is a directory, the directory is copied to a temporary directory.
The program runs Plaso analysis on the input file inside a Docker container.
The user is prompted whether to export the Super Timeline as a CSV file.
If the user selects to export, the program prompts the user to enter the path of the directory where they want to save the file.
The program runs Plaso export inside the Docker container and saves the output CSV file to the specified directory.
If the user does not select to export, the program exits.

## Usage:

- Ensure that Docker is installed and running on your system.
- Install the required Python modules by running ``` pip install -r requirements.txt.```
- Run the script by executing the following command in a terminal: ``` python plaso_analysis.py ```
- When prompted, enter the path of the file or directory you want to analyze.
- The program will run Plaso analysis on the file/directory inside a Docker container and display the output in the terminal.
- If you choose to export the Super Timeline as a CSV file, enter the path of the directory where you want to save the file.
- The program will save the output CSV file in the specified directory.
- If you choose not to export the Super Timeline, the program will exit.
