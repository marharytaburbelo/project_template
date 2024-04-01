

def main():
    pass


if __name__ == "__main__":
    main()

import input.py
import output.py

def main():
    text_from_console = input.input_text_from_console()
    file_path = "input_text_file.txt"
    output.write_text_to_file(text_from_console, file_path)
    output.output_text_to_console(text_from_console)
    text_from_file = input.read_text_from_file(file_path)
    output.output_text_to_console(text_from_file)
    output.write_text_to_file(text_from_file, "output_text_from_file.txt")
    text_from_file_with_pandas = input.read_text_from_file_with_pandas(file_path)
    output.output_text_to_console(text_from_file_with_pandas)
    output.write_text_to_file(text_from_file_with_pandas, "output_text_from_file_with_pandas.txt")


if __name__ == "__main__":
    def output_text_to_console(text):
        """
        Outputs text to the console.

        Args:
            text (str): The text to be output to the console.
        """
        print(text)


    def write_text_to_file(text, file_path):
        """
        Writes text to a file using Python's built-in capabilities.

        Args:
            text (str): The text to be written to the file.
            file_path (str): The path to the file where the text will be written.
        """
        try:
            with open(file_path, 'w') as file:
                file.write(text)
            print("Text has been written to the file successfully.")
        except Exception as e:
            print("An error occurred:", e)
    main()


