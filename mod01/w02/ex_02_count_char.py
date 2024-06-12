def count_char(text: str) -> dict[str, int]:
    """Count the frequency of each character in the given text."""
    frequency = {}
    for char in text:
        if char not in frequency:
            frequency[char] = 1
        else:
            frequency[char] += 1
    return frequency
