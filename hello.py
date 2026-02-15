def count_words_in_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            words = content.split()
        word_count = len(words)

        print(f"\nTotal number of words in '{filename}': {word_count}")

    except FileNotFoundError:
        print("Error: File not found. Please check the file name.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
print("===== Word Counter Program =====")

file_name = input("Enter the file name (with .txt extension): ")

count_words_in_file(file_name)
