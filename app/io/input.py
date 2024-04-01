import pandas as pd

def input_text_from_console():
    """
    Function to input text from the console.
    """
    text = input("Enter text from console: ")
    return text

def read_text_from_file(file_path):
    """
    Function to read text from a file using Python's built-in capabilities.
    """
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print("File not found.")
        return None

def read_text_from_file_with_pandas(file_path):
    """
    Function to read text from a file using the pandas library.
    """
    try:
        data = pd.read_csv(file_path)
        text = ' '.join(data.values.flatten())
        return text
    except FileNotFoundError:
        print("File not found.")
        return None
    if __name__ == "__main__":
        text_from_console = input_text_from_console()
        print("Text from console:", text_from_console)

        file_path = "text_file.txt"  # Replace with your own file path
        text_from_file = read_text_from_file(file_path)
        if text_from_file:
            print("Text from file:", text_from_file)

        text_from_file_with_pandas = read_text_from_file_with_pandas(file_path)
        if text_from_file_with_pandas:
            print("Text from file using pandas:", text_from_file_with_pandas)