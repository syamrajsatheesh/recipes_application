import csv




def save_data_to_csv(file_path, data):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def load_data_from_csv(file_path):
    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            data = [row for row in reader]
        return data
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return []

# Example data
example_data = [
    ["Name", "Age", "City"],
    ["John", 25, "New York"],
    ["Alice", 30, "San Francisco"],
    ["Bob", 22, "Los Angeles"]
]

# Save data to CSV
save_data_to_csv('example.csv', example_data)
print("Data saved to 'example.csv'")

# Load data from CSV
loaded_data = load_data_from_csv('example.csv')
print("\nLoaded Data:")
for row in loaded_data:
    print(row)