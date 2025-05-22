import os

# Get the current directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# List all files in the same folder
files = os.listdir(script_dir / "Data/Assets/Data_Game")

# Print all files
for file in files:
    print(file)