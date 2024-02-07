import pickle

def save_data_to_dat(file_path, data):
    try:
        # Load existing data from the pickle file
        with open(file_path, 'rb') as file:
            existing_data = pickle.load(file)
    except (FileNotFoundError, EOFError):
        # Handle the case where the file is not found or is empty
        existing_data = {}

    # Append new data to the existing data
    key = list(data.keys())
    existing_data[key[0]] = data[key[0]]

    # Write the updated data back to the pickle file
    with open(file_path, 'wb') as file:
        pickle.dump(existing_data, file)

def load_data_from_dat(file_path):
    try:
        with open(file_path, 'rb') as file:
            data = pickle.load(file)
        return data
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None

# Example data
example_data = {"me": "Syam"}

# Save data to DAT file
save_data_to_dat('example.dat', example_data)
print("Data saved to 'example.dat'")

# Load data from DAT file
loaded_data = load_data_from_dat('example.dat')
print("\nLoaded Data:")
print(loaded_data)