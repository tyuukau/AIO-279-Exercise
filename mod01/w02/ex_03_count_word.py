def count_word_in_file(file_path: str) -> dict[str, int]:
    """
    Count the frequency of each word in a file.

    Args:
        file_path (str): The path to the file.

    Returns:
        dict[str, int]: A dictionary where the keys are the words and the values are the frequencies.

    Notes:
        - This function handles the following exceptions internally:
            - FileNotFoundError: If the file is not found.
            - IOError: If an error occurs while reading the file.
    """
    try:
        with open(file_path, "r") as file:
            data = file.read().replace("\n", " ")
    except FileNotFoundError:
        print(f"Error: The file at '{file_path}' was not found.")
        return {}
    except IOError:
        print(f"Error: An IOError occurred while reading the file at '{file_path}'.")
        return {}

    frequency = {}
    word_list = data.split()
    for word in word_list:
        normalised_word = word.lower()
        if normalised_word not in frequency:
            frequency[normalised_word] = 1
        else:
            frequency[normalised_word] += 1

    return frequency
