import pickle





class EditFile:

    def __init__(self):
        self.data = None

    def write_to_file(key, value):
            try:
                # Load existing data from the pickle file
                with open("database.dat", 'rb') as file:
                    data = pickle.load(file)
            except (FileNotFoundError, EOFError):
                # Handle the case where the file is not found or is empty
                data = {}

            # Append new data to the existing data
            data[key] = value

            # Write the updated data back to the pickle file
            with open("database.dat", 'wb') as file:
                pickle.dump(data, file)
            return data


    def read_from_file():

        file_path = "database.dat"

        try:
            with open(file_path, 'rb') as file:
                data = pickle.load(file)

            return data
        
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")

