import pandas as pd
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Prompt the user for the CSV file locations and names with yellow text
print(Fore.YELLOW + "Enter the path to the first CSV file (with just emails): ", end="")
file1 = input()

print(Fore.YELLOW + "Enter the path to the second CSV file (with email, username, password, and hashed_password): ", end="")
file2 = input()

print(Fore.YELLOW + "Enter the name for the output CSV file (e.g., matching_rows.csv): ", end="")
output_file = input()

# Load the two CSV files
# The first CSV contains only email addresses
df_emails = pd.read_csv(file1, header=None, names=['email'])  # Assuming no header, just a list of emails
# The second CSV contains email, username, password, and hashed_password
df_data = pd.read_csv(file2)

# Convert the email column of df_emails into a set for faster lookup
email_set = set(df_emails['email'])

# Filter rows in df_data where the email exists in email_set
matching_rows = df_data[df_data['email'].isin(email_set)]

# Sort the matching rows by the 'email' column in alphabetical order
sorted_matching_rows = matching_rows.sort_values(by='email')

# Export the sorted matching rows to a new CSV file
sorted_matching_rows.to_csv(output_file, index=False)

# Completion message in green text
print(Fore.GREEN + "Wow...that was easy!")
print(Fore.GREEN + "Thank you for using the DehashedCompare script, used to compare a known good list of email accounts with what you dumped from Dehashed.com.")
print(Fore.GREEN + "You can buy me a coffee if you like this or send complaints and improvements to ChiefCyberPapa@proton.me.")
