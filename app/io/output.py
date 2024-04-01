def output_text_to_console(text):
    """
    Function to output text to the console.
    """
    print(text)

def write_text_to_file(text, file_path):
    """
    Function to write text to a file using Python's built-in capabilities.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(text)
        print("Text has been written to the file successfully.")
    except Exception as e:
        print("An error occurred:", e)
        if __name__ == "__main__":
            text = "This is a sample text."
            output_text_to_console(text)
file_path = "output_file.txt"
write_text_to_file("text", file_path)