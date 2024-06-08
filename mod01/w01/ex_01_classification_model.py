from typing import Any


def print_classification_metrics(tp: Any, fp: Any, fn: Any) -> None:
    """
    Prints Precision, Recall, and F1-score based on TP, FP, and FN.

    Args:
        tp (Any): True Positives. Must be an integer greater than 0.
        fp (Any): False Positives. Must be an integer greater than 0.
        fn (Any): False Negatives. Must be an integer greater than 0.

    Raises:
        TypeError: If any of tp, fp, or fn are not integers.
        ValueError: If any of tp, fp, or fn are less than or equal to 0.
    """
    if not isinstance(tp, int):
        raise TypeError("tp must be int")
    if not isinstance(fp, int):
        raise TypeError("tp must be int")
    if not isinstance(fn, int):
        raise TypeError("fn must be int")
    if not (tp > 0 and fp > 0 and fn > 0):
        raise ValueError("tp, fp, and fn should be greater than 0")

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1 = 2 * (precision * recall) / (precision + recall)

    print(f"Precision: {precision}")
    print(f"Recall: {recall}")
    print(f"f1-score: {f1}")


if __name__ == "__main__":
    try:
        print_classification_metrics(tp=2, fp=3, fn=4)
    except Exception as e:
        print(e)
