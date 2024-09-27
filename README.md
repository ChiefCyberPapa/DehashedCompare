# DehashedCompare
This is used to compare an export from DehashedExport (Find my export tool here: https://github.com/ChiefCyberPapa/DehashedExport/tree/main) with a list of known good emails, and find if any match with the DeHashed breaches database.

## Prerequisites

If you are coming here after using my DehashedExport script, then you have already met the prerequisites...so move onto installation.

Before using this script, ensure you have the following prerequisites installed:

1. **Python 3.x**: You need Python 3.x to run this script. You can check if Python is installed on your system by running:

   ```bash
   python3 --version
   ```

   If Python is not installed, install it using the following command for Ubuntu/Debian-based systems:

   ```bash
   sudo apt update
   ```
   ```bash
   sudo apt install python3 python3-pip
   ```

2. This script uses the colorama package to display colored text in the terminal. It also requires the pandas libray Install them by running:
   
   ```bash
   pip3 install colorama
   ```
   ```bash
   pip 3 install pandas
   ```

## Installation

1. Open the terminal and navigate to the directory where you want to store the script.

2. Use the git clone command to clone the repository:

   ```bash
   git clone https://github.com/ChiefCyberPapa/DehashedCompare.git
   ```
   
3. Navigate to the cloned directory:

   ```bash
   cd DehashedCompare
   ```
   
## Usage

Note: The script assumes you have a column on your email list CSV that you want to compare with, formatted with the column header name 'email'. It looks for this column header in case you have other columns with other data.

1. To run the script, follow these steps:

    In the terminal, navigate to the directory where the script is stored:

    ```bash
    cd path_to_directory/DehashedExport
    ```

2. Run the Python script:

    ```bash
    python3 DehashedCompare.py
    ```

3. python dehashed_compare.py

User Input: The script will prompt you for:

    The path to the first CSV file (with just emails).
    The path to the second CSV file (with email, username, password, and hashed_password).
    The name for the output CSV file where matching rows will be stored.

  Completion: Once the script runs, it will display a completion message and the output file will contain the matching rows sorted alphabetically by email.

4. Upon completion, the script will generate a matches.csv file with the rows that match the email addresses between the two input files

5. After successful completion, you will see a friendly message:

   Wow...that was easy!

   Thank you for using the DehashedCompare script, used to compare a known good list of email accounts with what you dumped from Dehashed.com.

   You can buy me a coffee if you like this or send complaints and improvements to ChiefCyberPapa@proton.me.

