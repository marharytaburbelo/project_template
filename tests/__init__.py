import unittest
import input.py

class TestReadTextFromFile(unittest.TestCase):
    def test_read_existing_file(self):
        file_path = "test_file.txt"
        expected_text = "This is a test text."
        with open(file_path, 'w') as file:
            file.write(expected_text)
        actual_text = input.read_text_from_file(file_path)
        self.assertEqual(actual_text, expected_text)

    def test_read_non_existing_file(self):
        file_path = "non_existing_file.txt"
        actual_text = input.read_text_from_file(file_path)
        self.assertIsNone(actual_text)

    def test_read_empty_file(self):
        file_path = "empty_file.txt"
        expected_text = ""

        with open(file_path, 'w') as file:
            file.write(expected_text)
        actual_text = input.read_text_from_file(file_path)
        self.assertEqual(actual_text, expected_text)

if __name__ == '__main__':
    unittest.main()

    import unittest
    import input
    import pandas as pd


    class TestReadTextFromFileWithPandas(unittest.TestCase):
        def test_read_existing_file(self):
            file_path = "test_file.csv"
            expected_text = "This is a test text."
            data = pd.DataFrame({"Text": [expected_text]})
            data.to_csv(file_path, index=False)

            actual_text = input.read_text_from_file_with_pandas(file_path)
            self.assertEqual(actual_text, expected_text)

        def test_read_non_existing_file(self):
            file_path = "non_existing_file.csv"
            actual_text = input.read_text_from_file_with_pandas(file_path)
            self.assertIsNone(actual_text)

        def test_read_empty_file(self):
            file_path = "empty_file.csv"
            expected_text = ""
            data = pd.DataFrame()
            data.to_csv(file_path, index=False)

            actual_text = input.read_text_from_file_with_pandas(file_path)
            self.assertEqual(actual_text, expected_text)


    if __name__ == '__main__':
        unittest.main()