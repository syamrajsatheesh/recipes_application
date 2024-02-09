import pickle





class EditFile:

    def __init__(self):
        self.data = None

    def write_to_file():
        pass


    def read_from_file():

        file_path = "database.dat"

        try:
            with open(file_path, 'rb') as file:
                data = pickle.load(file)

            return data
            items = list(data.keys())
        
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")

            