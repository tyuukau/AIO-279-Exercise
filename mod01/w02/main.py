from ex_01_max_in_sliding_window import max_in_sliding_window
from ex_02_count_char import count_char
from ex_03_count_word import count_word_in_file
from ex_04_levenshtein_distance import levenshtein_distance


def main():
    print("Demo max_in_sliding_window")
    try:
        for max_value in max_in_sliding_window([3, -1, -1, -1, -44, 5, 10, 12, 33, 1], 3):
            print(max_value)
    except Exception as e:
        print(e)

    print("Demo count_char")
    print(count_char("Happiness"))

    print("Demo count_word_in_file")
    result = count_word_in_file("./data/P1_data.txt")
    if result:
        print(result)

    print("Demo levenshtein_distance")
    s1 = "Hieu"
    s2 = "Hiu"
    distance = levenshtein_distance(s1=s1, s2=s2)
    print(distance)


if __name__ == "__main__":
    main()
